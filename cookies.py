import browser_cookie3

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
    except Exception as e:
        error.show_error_message(f'cannot find cookie for hoyolab.com, try logging in :::{e}')
    finally:
        return cookies