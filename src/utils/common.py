import os
from zipfile import ZipFile
import yaml
import logging
import time
import pandas as pd
import json
from zipfile import ZipFile

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        print(content)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    print(f"creating directories: {path_to_directories}")
    for path in path_to_directories:
        print(f"creating directory: {path}")
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")


def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")
def unzip_file(source:str,dest:str) ->None:
    with ZipFile(source, 'r') as zipObj:
        zipObj.extractall(dest)
    logging.info(f"unzipped file: {source} to: {dest}")