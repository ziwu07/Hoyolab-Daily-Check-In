import config
import cookies
import api_calls

genshin_ref_url = f"https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id={config.GENSHIN_ACT_ID}"
genshin_req_url = f"https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us&act_id={config.GENSHIN_ACT_ID}"
star_rail_ref_url = f"https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id={config.STAR_RAIL_ACT_ID}"
star_rail_req_url = f"https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id={config.STAR_RAIL_ACT_ID}"
_config = config.load()


if __name__ == "__main__":
    cookie = cookies.get_cookies()
    if _config.genshin:
        api_calls.claim(req_url=genshin_req_url, ref_url=genshin_ref_url, cookie=cookie)
    if _config.star_rail:
        api_calls.claim(
            req_url=star_rail_req_url, ref_url=star_rail_ref_url, cookie=cookie
        )
