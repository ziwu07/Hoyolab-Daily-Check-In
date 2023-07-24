import json
import os

CONFIG_FILE_PATH = "config.json"

def create_default_config():
    default_config = {
        'browser': 'all',
        'schedule_name': 'Genshin Check In',
        'delay_minute': 1,
        'run_time(24h)': 12,
        'reset_timezone(UTC)': '08'
    }
    return default_config

def write_config(config):
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump(config, config_file, indent=4)

def read_config():
    if not os.path.exists(CONFIG_FILE_PATH):
        config = create_default_config()
        write_config(config)
    else:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config = json.load(config_file)
        default_config = create_default_config()
        for key, value in default_config.items():
            if key not in config:
                config[key] = value
        write_config(config)

    return config

def update_config(key, value):
    config = read_config()
    config[key] = value
    write_config(config)
