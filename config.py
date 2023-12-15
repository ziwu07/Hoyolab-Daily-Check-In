import json
import os

CONFIG_FILE_PATH = "config.json"

default_config = {
    "browser": "all",
    "schedule_name": "Hoyolab Check In",
    "delay_minute": 1,
    "run_time(24h)": 12,
    "random_delay": 5,
}


def write_config(config: dict[str, any]):
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump(config, config_file, indent=4)


def read_config():
    if not os.path.exists(CONFIG_FILE_PATH):
        config = default_config
        write_config(config)
    else:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config = json.load(config_file)
        for key, value in default_config.items():
            if key not in config:
                config[key] = value
        write_config(config)
    return config


def update_config(key, value):
    config = read_config()
    config[key] = value
    write_config(config)
