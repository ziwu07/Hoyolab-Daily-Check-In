from http.cookiejar import CookieJar
from typing import Any
import requests
from urllib3 import Retry
import error
from json import loads


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


def api_call(req_url: str, ref_url: str, cookie: CookieJar) -> dict[str, Any]:
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Origin": "https://act.hoyolab.com",
        "Referer": ref_url,
    }
    try:
        response = requests.post(
            req_url,
            headers=headers,
            cookies=requests.sessions.RequestsCookieJar().update(cookie),
        )
        return dict[str, Any](loads(response.json()))
    except requests.ConnectionError:
        error.crash("Connection err")
    except requests.Timeout:
        error.crash("Connection timeout")
    except requests.exceptions.RequestException:
        error.crash("unknown network err")
