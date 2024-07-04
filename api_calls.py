from http.cookiejar import CookieJar, DefaultCookiePolicy
from typing import Any
from urllib import request
from http import HTTPMethod
from config import USER_AGENT
import json
import ssl
import error
import cookies


def claim(**args):
    resp = api_call(**args)
    match resp["retcode"]:
        case -100:
            error.log(str(resp["message"]), "warn")
            args["cookie"] = cookies.get_cookies(force=True)
            claim(**args)
        case 0:
            return
        case _:
            error.log(str(resp), "warn")
    return


def api_call(
    req_url: str, ref_url: str, cookie: CookieJar, data: None | dict = None
) -> dict[str, Any]:
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "User-Agent": USER_AGENT,
        "Origin": "https://act.hoyolab.com",
        "Referer": ref_url,
    }
    policy = DefaultCookiePolicy()
    policy.hide_cookie2 = True
    cookie.set_policy(policy=policy)
    _request = request.Request(
        url=req_url, headers=headers, method=HTTPMethod.POST, data=data
    )
    cookie.add_cookie_header(_request)
    ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
    with request.urlopen(_request, context=ssl_context) as resp:
        return dict(json.loads(resp.read()))
