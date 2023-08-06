from __future__ import print_function
import sys
import os.path
from pathlib import Path
import re
import glob
from datetime import datetime
import logging
import pystache
from . import nfs_mount_parse
import sdap_ingest_manager.granule_ingester
from sdap_ingest_manager.history_manager import md5sum_from_filepath


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

GROUP_PATTERN = "(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?"
GROUP_DEFAULT_NAME = "group default name"

DEFAULT_DATA_FILE_EXTENSION = ['nc', 'h5']


def is_in_time_range(file, ts_from, ts_to):
    """
    :param file: file path as a string
    :param ts_from: timestamp, can be None
    :param ts_to: timestamp, can be None
    :return: True is the update time of the file is between ts_from and ts_to. False otherwise
    """
    file_mtimestamp = os.path.getmtime(file)
    status_from = True
    if ts_from:
        if ts_from < file_mtimestamp:
            status_from = True
        else:
            status_from = False

    status_to = True
    if ts_to:
        if ts_to > file_mtimestamp:
            status_to = True
        else:
            status_to = False

    return status_from and status_to


def get_file_list(file_path_pattern):
    """

    :param file_path_pattern: regular expression or directory which will be extended with default extensions (nc, h5, ...)
    :return: the list of files matching
    """
    logger.info("get files matching %s", file_path_pattern)
    file_path_pattern = os.path.join(sys.prefix, '.sdap_ingest_manager', file_path_pattern)
    logger.info("from sys.prefix directory for relative path %s", file_path_pattern)
    if os.path.isdir(file_path_pattern):
        file_list = []
        for extension in DEFAULT_DATA_FILE_EXTENSION:
            extended_file_path_pattern = os.path.join(file_path_pattern, f'*.{extension}')
            file_list.extend(glob.glob(extended_file_path_pattern))
    else:
        file_list = glob.glob(file_path_pattern)

    logger.info("%i files found", len(file_list))

    return file_list


def create_granule_list(file_path_pattern, dataset_ingestion_history_manager,
                        granule_list_file_path, deconstruct_nfs=False,
                        date_from=None, date_to=None,
                        forward_processing=False):
    """ Creates a granule list file from a file path pattern
        matching the granules.
        If a granules has already been ingested with same md5sum signature, it is not included in this list.
        When deconstruct_nfs is True, the paths will shown as viewed on the nfs server
        and not as they are mounted on the nfs client where the script runs (default behaviour).
    """

    file_list = get_file_list(file_path_pattern)

    logger.info("Create granule list file %s", granule_list_file_path)
    dir_path = os.path.dirname(granule_list_file_path)
    logger.info("Granule list file created in directory %s", dir_path)
    Path(dir_path).mkdir(parents=True, exist_ok=True)

    if forward_processing:
        if dataset_ingestion_history_manager:
            timestamp_from = dataset_ingestion_history_manager.get_latest_ingested_file_update()
        if dataset_ingestion_history_manager is None or timestamp_from is None:
            logger.info("No ingestion history available, forward processing ignored")
            timestamp_from = None
        timestamp_to = None
    else:
        timestamp_from = date_from.timestamp() if date_from else None
        timestamp_to = date_to.timestamp() if date_to else None

    if deconstruct_nfs:
        mount_points = nfs_mount_parse.get_nfs_mount_points()

    with open(granule_list_file_path, 'w') as file_handle:
        for file_path in file_list:
            if is_in_time_range(file_path, timestamp_from, timestamp_to):
                filename = os.path.basename(file_path)
                already_ingested = False
                if dataset_ingestion_history_manager:
                    logger.info(f"is file {file_path} already ingested ?")
                    already_ingested = dataset_ingestion_history_manager.has_valid_cache(file_path)
                if not already_ingested:
                    logger.info(f"file {filename} not ingested yet, added to the list")
                    if deconstruct_nfs:
                        file_path = nfs_mount_parse.replace_mount_point_with_service_path(file_path, mount_points)
                    file_handle.write(f'{file_path}\n')
                else:
                    logger.debug(f"file {filename} already ingested with same md5sum")
            else:
                logger.debug(f"file {file_path} has not been updated in the targeted time range")


def create_dataset_config(collection_id, variable_name, collection_config_template, target_config_file_path):
    logger.info("Create dataset configuration file %s", target_config_file_path)
    renderer = pystache.Renderer()
    collection_config_template_path = os.path.join(sys.prefix, collection_config_template)
    config_content = renderer.render_path(collection_config_template_path, {'dataset_id': collection_id,
                                                            'variable': variable_name})
    logger.info("templated dataset config \n%s", config_content)

    dir_path = os.path.dirname(target_config_file_path)
    logger.info("Dataset configuration file created in directory %s", dir_path)
    Path(dir_path).mkdir(parents=True, exist_ok=True)

    with open(target_config_file_path, "w") as f:
        f.write(config_content)


def collection_row_callback(collection,
                            collection_config_template,
                            granule_file_list_root_path,
                            dataset_configuration_root_path,
                            history_root_path,
                            deconstruct_nfs=False,
                            **pods_run_kwargs
                            ):
    """ Create the configuration and launch the ingestion
        for the given collection row
    """
    dataset_id = collection['id']
    netcdf_variable = collection['variable']
    netcdf_file_pattern = collection['path']

    if 'forward_processing' in collection.keys():
        forward_processing = collection['forward_processing']
    else:
        forward_processing = False

    granule_list_file_path = os.path.join(granule_file_list_root_path,
                                          f'{dataset_id}-granules.lst')
    dataset_ingestion_history_manager = sdap_ingest_manager.history_manager\
        .DatasetIngestionHistoryFile(history_root_path, dataset_id, lambda x: str(os.path.getmtime(x)))


    time_range = {}
    for time_boundary in {"from", "to"}:
        if time_boundary in collection.keys() and collection[time_boundary]:
            # add prefix "from" because is a reserved name which can not be used as function argument
            time_range[f'date_{time_boundary}'] = datetime.fromisoformat(collection[time_boundary])
            logger.info(f"time criteria {time_boundary} is {time_range[f'date_{time_boundary}']}")

    create_granule_list(netcdf_file_pattern,
                        dataset_ingestion_history_manager,
                        granule_list_file_path,
                        deconstruct_nfs=deconstruct_nfs,
                        **time_range,
                        forward_processing=forward_processing)

    dataset_configuration_file_path = os.path.join(dataset_configuration_root_path,
                                                   f'{dataset_id}-config.yml')

    create_dataset_config(dataset_id,
                          netcdf_variable,
                          collection_config_template,
                          dataset_configuration_file_path)
    cwd = os.getcwd()
    # group must match the following regex (([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?
    # and when suffixed with uid must not exceed 64 characters
    prog = re.compile(GROUP_PATTERN)
    group = prog.match(dataset_id[:19])
    if group is None:
        group_name = GROUP_DEFAULT_NAME
    else:
        group_name = group.group(0)
    pods_run_kwargs['file_list_path'] = granule_list_file_path
    pods_run_kwargs['job_config'] = dataset_configuration_file_path
    pods_run_kwargs['job_group'] = group_name
    pods_run_kwargs['ningester_version'] = '1.1.0'
    pods_run_kwargs['delete_successful'] = True
    pods_run_kwargs['hist_manager'] = dataset_ingestion_history_manager

    def param_to_str_arg(k, v):
        k_with_dash = k.replace('_', '-')
        str_k = f'--{k_with_dash}'
        if type(v) == bool:
            if v:
                return [str_k]
            else:
                return []
        elif isinstance(v, list):
            return [str_k, ','.join(v)]
        else:
            return [str_k, str(v)]

    pod_launch_options = [param_to_str_arg(k, v) for (k,v) in pods_run_kwargs.items()]
    flat_pod_launch_options = [item for option in pod_launch_options for item in option]
    pod_launch_cmd = ['run_granules'] + flat_pod_launch_options
    logger.info("launch pod with command:\n%s", " ".join(pod_launch_cmd))
    sdap_ingest_manager.granule_ingester.create_and_run_jobs(**pods_run_kwargs)


