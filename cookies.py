from typing import Callable
import browser_cookie3
import error
from http.cookiejar import CookieJar, LWPCookieJar
import config

COOKIE_FILE = "./cookies.pkl"


def get_cookies(browser: config.Browser, domain_name: str) -> CookieJar:
    from_browser = get_from_browser(browser=browser, domain_name=domain_name)
    if from_browser != None:
        pass
    pass


def get_from_browser(browser: config.Browser, domain_name: str) -> CookieJar | None:
    browser_functions: dict[config.Browser, Callable[..., CookieJar]] = {
        config.Browser.ALL: browser_cookie3.load,
        config.Browser.CHROME: browser_cookie3.chrome,
        config.Browser.CHROMIUM: browser_cookie3.chromium,
        config.Browser.OPERA: browser_cookie3.opera,
        config.Browser.OPERA_GX: browser_cookie3.opera_gx,
        config.Browser.BRAVE: browser_cookie3.brave,
        config.Browser.EDGE: browser_cookie3.edge,
        config.Browser.VIVALDI: browser_cookie3.vivaldi,
        config.Browser.FIREFOX: browser_cookie3.firefox,
        config.Browser.LIBREWOLF: browser_cookie3.librewolf,
        config.Browser.SAFARI: browser_cookie3.safari,
    }
    try:
        cookie_function = browser_functions.get(browser)
        if cookie_function is not None:
            return cookie_function(domain_name=domain_name)
        else:
            return error.crash("no browser defined")
    except Exception as e:
        error.log(f"cannot find cookie for hoyolab.com : {e}", "warn")
        return None
