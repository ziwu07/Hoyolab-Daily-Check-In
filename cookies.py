import browser_cookie3
import error
from http.cookiejar import CookieJar
import pickle

COOKIE_FILE = "./cookies.pkl"


def get_cookies(browser: str, domain_name: str) -> CookieJar:
    from_browser = get_from_browser(browser=browser, domain_name=domain_name)
    try:
        with open(COOKIE_FILE, "rb+") as file:
            if from_browser != None:
                pickle.dump(from_browser, file)
                return from_browser
            else:
                return pickle.load(file)
    except FileNotFoundError:
        with open(COOKIE_FILE, "xb") as file:
            if from_browser == None:
                return error.crash("unable to get cookie from browser")
            else:
                pickle.dump(from_browser, file)
                return from_browser


def get_from_browser(browser: str, domain_name: str) -> CookieJar | None:
    try:
        if browser.lower() == "all":
            cookies = browser_cookie3.load(domain_name=domain_name)
        elif browser.lower() == "firefox":
            cookies = browser_cookie3.firefox(domain_name=domain_name)
        elif browser.lower() == "chrome":
            cookies = browser_cookie3.chrome(domain_name=domain_name)
        elif browser.lower() == "opera":
            cookies = browser_cookie3.opera(domain_name=domain_name)
        elif browser.lower() == "edge":
            cookies = browser_cookie3.edge(domain_name=domain_name)
        elif browser.lower() == "chromium":
            cookies = browser_cookie3.chromium(domain_name=domain_name)
        elif ("opera" in browser) and ("gx" in browser):
            cookies = browser_cookie3.opera_gx(domain_name=domain_name)
        else:
            return error.crash("no browser defined")
        return cookies
    except Exception as e:
        error.log(f"cannot find cookie for hoyolab.com : {e}", "warn")
        return None
