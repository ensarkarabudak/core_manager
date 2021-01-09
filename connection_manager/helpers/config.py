import yaml
import os
from helpers.logger import initialize_logger

logger = initialize_logger(True)

CM_PATH = os.path.expanduser("~") + "/connection_manager/"
CONFIG_PATH = CM_PATH + "config.yaml"
SYSTEM_PATH = CM_PATH + "system.yaml"

def read_yaml_with_key(file, key):
    pass

def update_yaml_with_key(file, key, value):
    pass

def read_yaml_all(file):
    with open(file) as f:
        data = yaml.safe_load(f)
        return data

def write_yaml_all(file, items, clear = True):
    if clear == True:
        with open(file, 'w') as f:
            yaml.dump(items, f, default_flow_style=False)
    else:
        with open(file, 'a') as f:
            yaml.dump(items, f, default_flow_style=False)

