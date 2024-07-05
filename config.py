import json
from dataclasses import dataclass, asdict

CONFIG_FILE_PATH = "./config.json"
COOKIE_FILE_PATH = "./Cookies"
GENSHIN_ACT_ID = "e202102251931481"
STAR_RAIL_ACT_ID = "e202303301540311"
ZZZ_ACT_ID = "e202406031448091"

GENSHIN_REF_URL = (
    f"https://act.hoyolab.com/ys/event/signin-sea-v3/"
    f"index.html?act_id={GENSHIN_ACT_ID}"
)
GENSHIN_REQ_URL = (
    f"https://sg-hk4e-api.hoyolab.com/event/sol/"
    f"sign?lang=en-us&act_id={GENSHIN_ACT_ID}"
)
STAR_RAIL_REF_URL = (
    f"https://act.hoyolab.com/bbs/event/signin/hkrpg/"
    f"index.html?act_id={STAR_RAIL_ACT_ID}"
)
STAR_RAIL_REQ_URL = (
    "https://sg-public-api.hoyolab.com/event/luna/os/"
    f"sign?lang=en-us&act_id={STAR_RAIL_ACT_ID}"
)
ZZZ_REF_URL = (
    f"https://act.hoyolab.com/bbs/event/signin/zzz/"
    f"{ZZZ_ACT_ID}.html?act_id={ZZZ_ACT_ID}"
)
ZZZ_REQ_URL = (
    f"https://sg-act-nap-api.hoyolab.com/event/luna/zzz/os/"
    f"sign?lang=en-us&act_id={ZZZ_ACT_ID}"
)

LOGIN_URI = GENSHIN_REF_URL
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)


@dataclass()
class Config:
    star_rail: bool = True
    genshin: bool = True
    zzz: bool = True


def load() -> "Config":
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config_data = json.load(config_file)
            return Config(**config_data)
    except FileNotFoundError:
        with open(CONFIG_FILE_PATH, "x") as config_file:
            json.dump(asdict(Config()), config_file, indent=4)
        return Config()
