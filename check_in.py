import cookies
import api_calls
import multiprocessing
import error
from config import *

_config = load()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    cookie = cookies.get_cookies()
    if _config.genshin:
        api_calls.claim(req_url=GENSHIN_REQ_URL, ref_url=GENSHIN_REF_URL,
                        cookie=cookie)
    if _config.star_rail:
        api_calls.claim(
            req_url=STAR_RAIL_REQ_URL, ref_url=STAR_RAIL_REF_URL, cookie=cookie
        )
    error.log("checked in")
