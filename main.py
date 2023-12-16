import config
import cookies
import api_calls

domain_name = ".hoyolab.com"
genshin_act_id = "e202102251931481"
star_rail_act_id = "e202303301540311"

genshin_ref_url = f"https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id={genshin_act_id}"
genshin_req_url = f"https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us&act_id={genshin_act_id}"
star_rail_ref_url = f"https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id={star_rail_act_id}"
star_rail_req_url = f"https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id={star_rail_act_id}"
_config = config.read_config()


if __name__ == "__main__":
    cookie = cookies.get_cookies(browser=_config["browser"], domain_name=domain_name)
    api_calls.claim(req_url=genshin_req_url, ref_url=genshin_ref_url, cookie=cookie)
    api_calls.claim(req_url=star_rail_req_url, ref_url=star_rail_ref_url, cookie=cookie)
