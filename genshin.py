import requests
import error


def Claim(act_id: str, cookie: dict):
    resp = api_call(act_id=act_id, cookie=cookie)
    if (
        str(resp["retcode"]) == "-5003"
        and str(resp["message"]) == "Traveler, you've already checked in today~"
    ):
        return True
    elif (
        str(resp["retcode"]) == "0"
        and str(resp["data"]["gt_result"]["is_risk"]) == "True"
    ):
        error.show_error_message("is_risk = true")
    elif str(resp["retcode"]) == "0":
        return False
    else:
        error.show_error_message("at response code for claimReward()")


def api_call(act_id: str, cookie: dict):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Origin": "https://act.hoyolab.com",
        "Referer": f"https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id={act_id}",
    }
    try:
        response = requests.post(
            f"https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us&act_id={act_id}",
            headers=headers,
            cookies=cookie,
        )
        return response.json()
    except Exception as e:
        error.show_error_message(f"at claimReward() requests.post :::{e}")
