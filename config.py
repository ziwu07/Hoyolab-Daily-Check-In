import json
import os
from typing import Any

CONFIG_FILE_PATH = "config.json"

default_config: dict[str, Any] = {
    "browser": "all",
    "star_rail": True,
    "genshin": True,
    "schedule_name": "Hoyolab Check In",
    "delay_minute": 1,
    "run_time(24h)": 12,
    "random_delay": 5,
}


def write_config(config: dict[str, Any]):
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump(config, config_file, indent=4)


def read_config() -> dict[str, Any]:
    if not os.path.exists(CONFIG_FILE_PATH):
        config = default_config
        write_config(config)
    else:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config = dict[str, Any](json.load(config_file))
        for key, value in default_config.items():
            if key not in config:
                config[key] = value
        write_config(config)
    return config
