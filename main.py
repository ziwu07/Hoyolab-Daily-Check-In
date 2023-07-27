import browser_cookie3
import os
import genshin
import star_rail
import error
import config

domain_name = '.hoyolab.com'
genshin_act_id = 'e202102251931481'
star_rail_act_id= 'e202303301540311'
_config = config.read_config()

def GetToken(browser:str, domain_name:str):
    try:
        if browser.lower() == 'all':
            cookies = browser_cookie3.load(domain_name=domain_name)
        elif browser.lower() == 'firefox':
            cookies = browser_cookie3.firefox(domain_name=domain_name)
        elif browser.lower() == 'chrome':
            cookies = browser_cookie3.chrome(domain_name=domain_name)
        elif browser.lower() == 'opera':
            cookies = browser_cookie3.opera(domain_name=domain_name)
        elif browser.lower() == 'edge':
            cookies = browser_cookie3.edge(domain_name=domain_name)
        elif browser.lower() == 'chromium':
            cookies = browser_cookie3.chromium(domain_name=domain_name)
        elif ('opera' in browser) and ('gx' in browser):
            cookies = browser_cookie3.opera_gx(domain_name=domain_name)
        else:
            error.show_error_message('no browser defined')
        cookie_name = ['ltoken', 'ltuid','ltoken_v2','ltuid_v2']
        token = {}
        for cookie in cookies:
            if cookie.name in cookie_name:
                token[cookie.name] = cookie.value
        return token
    except Exception as e:
        error.show_error_message(f'cannot find cookie for hoyolab.com, try logging in :::{e}')

if __name__ == "__main__":
    token = GetToken(browser=_config['browser'], domain_name=domain_name)
    genshin.Claim(act_id=genshin_act_id, cookie=token)
    star_rail.Claim(act_id=star_rail_act_id, cookie=token)
    