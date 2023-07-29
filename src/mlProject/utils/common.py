import os

from box.exceptions import BoxValueError
import  yaml
from src.mlProject.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox

from pathlib import Path
from typing import  Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully ')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as ex:
        raise ex


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):

    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'created directory :{path}')
    except BoxValueError:
        raise ValueError
    except Exception as ex:
        raise ex


@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
    except BoxValueError:
        raise ValueError
    except Exception as ex:
        raise ex


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as file:
            content = json.load(file)
        logger.info(f'json file loaded successfully from: {path}')
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError
    except Exception as ex:
        raise ex


@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data,
                    filename =path)
        logger.info(
            f'binary file saved at : {path}'
        )

    except BoxValueError:
        raise ValueError
    except Exception as ex:
        raise ex


@ensure_annotations
def load_bin(path: Path) -> Any:

    data = joblib.load(filename=path)
    logger.info(f'binary file loaded successfully')
    return data


@ensure_annotations
def get_size(path: Path) -> str:

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} kb"
