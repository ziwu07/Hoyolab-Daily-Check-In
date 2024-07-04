import json
from dataclasses import dataclass, asdict

CONFIG_FILE_PATH = "./config.json"
COOKIE_FILE_PATH = "./Cookies"
GENSHIN_ACT_ID = "e202102251931481"
STAR_RAIL_ACT_ID = "e202303301540311"

GENSHIN_REF_URL = (
    f"https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=\
            {GENSHIN_ACT_ID}"
)
GENSHIN_REQ_URL = (
    f"https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us&act_id=\
            {GENSHIN_ACT_ID}"
)
STAR_RAIL_REF_URL = f"https://act.hoyolab.com/bbs/event/signin/hkrpg/\
        index.html?act_id={STAR_RAIL_ACT_ID}"
STAR_RAIL_REQ_URL = f"https://sg-public-api.hoyolab.com/event/luna/os/\
        sign?lang=en-us&act_id={STAR_RAIL_ACT_ID}"

LOGIN_URI = GENSHIN_REF_URL


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
