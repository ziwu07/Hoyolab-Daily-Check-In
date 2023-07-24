import requests
import error

def Claim(act_id:str, cookie:dict):
    resp = requests_post(act_id=act_id, cookie=cookie)
    if str(resp['retcode']) == '-5003' and str(resp['message']) == "You've already checked in today, Trailblazer~":
        return True
    elif str(resp['retcode']) == '0' and str(resp['data']['gt_result']['is_risk']) == 'True':
        error.show_error_message('please relogin at hoyolab.com')
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
        'Referer': f'https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id={act_id}&lang=en-us',
    }
    try:
        response = requests.post(f'https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id={act_id}', headers=headers, cookies=cookie,)
        return response.json()
    except Exception as e:
        error.show_error_message(f'at claimReward() requests.post :::{e}')
