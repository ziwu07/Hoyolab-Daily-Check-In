from http.cookies import SimpleCookie
from config import USER_AGENT
import os
import webview

storage_path = os.path.join(os.getcwd(), "webview_storage")


def lauch_webview(uri: str) -> list[SimpleCookie] | None:
    def get_cookies():
        nonlocal _cookies
        _cookies = window.get_cookies()
        window.destroy()

    def quit():
        nonlocal _cookies
        window.destroy()
        _cookies = None

    _cookies = []
    window = webview.create_window(title="hoyo login", url=uri)
    menu = [
        webview.menu.Menu(
            "Actions",
            [
                webview.menu.MenuAction("Get Cookies", get_cookies),
                webview.menu.MenuAction("Quit", quit),
            ],
        )
    ]
    webview.start(
        user_agent=USER_AGENT,
        private_mode=False,
        storage_path=storage_path,
        gui="qt",
        menu=menu,
    )
    return _cookies
