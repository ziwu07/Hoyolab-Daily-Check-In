import requests
import error

def Claim(act_id:str, cookie:dict):
    resp = requests_post(act_id=act_id, cookie=cookie)
    if str(resp['retcode']) == '-5003' and str(resp['message']) == "Traveler, you've already checked in today~":
        return True
    elif str(resp['retcode']) == '0':
        return False
    else:
        error.show_error_message('at response code for claimReward()')
    
def requests_post(act_id:str, cookie:dict):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://act.hoyolab.com',
        'Referer': f'https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id={act_id}&lang=en-us',
    }
    try:
        response = requests.post(f'https://hk4e-api-os.hoyolab.com/event/sol/sign?lang=en-us&act_id={act_id}', headers=headers, cookies=cookie,)
        return response.json()
    except Exception as e:
        error.show_error_message(f'at claimReward() requests.post :::{e}')
