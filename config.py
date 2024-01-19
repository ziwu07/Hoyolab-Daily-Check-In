import json
from dataclasses import dataclass, asdict

CONFIG_FILE_PATH = "./config.json"
COOKIE_FILE_PATH = "./Cookies"
LOGIN_URI = "https://account.hoyolab.com/#/login"
GENSHIN_ACT_ID = "e202102251931481"
STAR_RAIL_ACT_ID = "e202303301540311"


@dataclass()
class Config:
    star_rail: bool = True
    genshin: bool = True


def load() -> "Config":
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config_data = json.load(config_file)
            return Config(**config_data)
    except FileNotFoundError:
        with open(CONFIG_FILE_PATH, "x") as config_file:
            json.dump(asdict(Config()), config_file, indent=4)
        return Config()
