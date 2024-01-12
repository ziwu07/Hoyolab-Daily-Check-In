from http.cookiejar import CookieJar
from http.cookies import SimpleCookie
import os
import webview

storage_path = os.path.join(os.getcwd(), "webview_storage")


def get_cookies(domain_name: str):
    pass


def lauch_webview(uri: str):
    _cookies = None
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

    def closing():
        nonlocal _cookies
        _cookies = window.get_cookies()
        window.destroy()

    window = webview.create_window(title="hoyo login", url=uri, confirm_close=True)
    window.events.closing += closing
    webview.start(
        user_agent=user_agent,
        private_mode=False,
        storage_path=storage_path,
        gui="edgechromium",
    )
    return _cookies
