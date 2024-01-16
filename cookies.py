import http.cookiejar, _webview, calendar, time
from config import COOKIE_FILE_PATH


def get_cookies(uri):
    cookies = http.cookiejar.LWPCookieJar(COOKIE_FILE_PATH)
    try:
        cookies.load()
    except FileNotFoundError:
        cookies = get_cookies_webview(uri)
        cookies.save()
    if not cookies:
        cookies = get_cookies_webview(uri)
        cookies.save()
    return cookies


def get_cookies_webview(uri):
    cookie = _webview.lauch_webview(uri)
    cookies = http.cookiejar.LWPCookieJar(COOKIE_FILE_PATH)
    for c in cookie:
        for k, v in c.items():
            cookies.set_cookie(morsel_to_cookie(v))
    return cookies


def morsel_to_cookie(morsel):
    """code from https://github.com/psf/requests"""

    expires = None
    if morsel["max-age"]:
        try:
            expires = int(time.time() + int(morsel["max-age"]))
        except ValueError:
            raise TypeError(f"max-age: {morsel['max-age']} must be integer")
    elif morsel["expires"]:
        time_template = "%a, %d %b %Y %H:%M:%S GMT"
        expires = calendar.timegm(time.strptime(morsel["expires"], time_template))
    result = {
        "version": 0,
        "name": morsel.key,
        "value": morsel.value,
        "port": None,
        "domain": "",
        "path": "/",
        "secure": False,
        "expires": None,
        "discard": True,
        "comment": None,
        "comment_url": None,
        "rest": {"HttpOnly": None},
        "rfc2109": False,
    }
    result.update(
        comment=morsel["comment"],
        comment_url=bool(morsel["comment"]),
        discard=False,
        domain=morsel["domain"],
        expires=expires,
        path=morsel["path"],
        port=None,
        rest={"HttpOnly": morsel["httponly"]},
        rfc2109=False,
        secure=bool(morsel["secure"]),
        version=morsel["version"] or 0,
    )
    result["port_specified"] = bool(result["port"])
    result["domain_specified"] = bool(result["domain"])
    result["domain_initial_dot"] = result["domain"].startswith(".")
    result["path_specified"] = bool(result["path"])
    return http.cookiejar.Cookie(**result)
