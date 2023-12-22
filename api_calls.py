from http.cookiejar import CookieJar, DefaultCookiePolicy
from typing import Any
from urllib import request
from http import HTTPMethod
import error
import json
import ssl
import certifi


def claim(req_url: str, ref_url: str, cookie: CookieJar) -> bool:
    resp = api_call(req_url=req_url, ref_url=ref_url, cookie=cookie)
    if str(resp["retcode"]) == "-5003":
        return True
    elif str(resp["retcode"]) == "0":
        if str(resp["data"]["gt_result"]["is_risk"]) == "True":
            error.show_error_message("capcha triggered")
            return False
        else:
            return False
    elif str(resp["retcode"]) == "-100":
        error.crash("not logged in")
    else:
        return False


def api_call(
    req_url: str, ref_url: str, cookie: CookieJar
) -> tuple[list[tuple[str, str]], dict[str, Any]]:
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Origin": "https://act.hoyolab.com",
        "Referer": ref_url,
    }
    policy = DefaultCookiePolicy()
    policy.hide_cookie2 = True
    cookie.set_policy(policy=policy)
    _request = request.Request(url=req_url, headers=headers, method=HTTPMethod.POST)
    cookie.add_cookie_header(_request)
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    with request.urlopen(_request, context=ssl_context) as resp:
        return (resp.getheaders(), dict(json.loads(resp.read())))
