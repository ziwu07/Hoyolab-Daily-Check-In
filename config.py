import json
import error
from typing import Any
from dataclasses import dataclass
from enum import Enum

CONFIG_FILE_PATH = "./config.json"


class Browser(Enum):
    ALL = "all"
    CHROME = "chrome"
    CHROMIUM = "chromium"
    OPERA = "opera"
    OPERA_GX = "opera_gx"
    BRAVE = "brave"
    EDGE = "edge"
    VIVALDI = "vivaldi"
    FIREFOX = "firefox"
    LIBREWOLF = "librewolf"
    SAFARI = "safari"


@dataclass()
class Config:
    browser: Browser = Browser.ALL
    star_rail: bool = True
    genshin: bool = True
    schedule_name: str = "Hoyolab Check In"
    delay_minute: int = 1
    run_time_24h: int = 12
    random_delay: int = 5


def load() -> "Config":
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config_data: dict[str, Any] = json.load(config_file)
            config_data["browser"] = Browser(config_data["browser"])
        return Config(**config_data)
    except ValueError:
        return error.crash("invalid browser name")
