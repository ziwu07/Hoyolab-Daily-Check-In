import json
from typing import Any
from dataclasses import dataclass

CONFIG_FILE_PATH = "./config.json"


@dataclass()
class Config:
    star_rail: bool = True
    genshin: bool = True
    schedule_name: str = "Hoyolab Check In"
    delay_minute: int = 1
    run_time_24h: int = 12
    random_delay: int = 5


def load() -> "Config":
    with open(CONFIG_FILE_PATH, "r") as config_file:
        config_data: dict[str, Any] = json.load(config_file)
    return Config(**config_data)
