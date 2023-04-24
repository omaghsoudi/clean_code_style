#!/usr/bin/python3

import json
import tarfile
from copy import deepcopy
from logging import Logger
from argparse import Namespace


def _creat_dict_from_namespace(name_space_dict):
    for key in name_space_dict.keys():
        value = name_space_dict[key]
        if isinstance(value, Namespace):
            name_space_dict[key] = _creat_dict_from_namespace(value.__dict__)
    return name_space_dict


def print_variables(config: Namespace, logger: Logger):
    """

    Args:
        config:
        logger:

    Returns:
        None

    """
    print_config = deepcopy(config)
    logger.info("Printing the updated Config:")
    logger.info(json.dumps(_creat_dict_from_namespace(print_config.__dict__), indent=2, default=str))


def read_tar_file(path_to_file: str, logger:Logger):
    logger.info("loading the variables:")
    tar = tarfile.open(path_to_file, "r:gz")
    for member in tar.getmembers():
        f = tar.extractfile(member)
        if f is not None:
            content = f.read()
            logger.info(content)