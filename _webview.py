from http.cookies import SimpleCookie
import os, webview, webview.menu

storage_path = os.path.join(os.getcwd(), "webview_storage")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"


def lauch_webview(uri: str) -> list[SimpleCookie]:
    def get_cookies():
        nonlocal _cookies
        _cookies = window.get_cookies()
        window.destroy()

    _cookies = []
    window = webview.create_window(title="hoyo login", url=uri)
    menu = [
        webview.menu.Menu(
            "Cookies",
            [webview.menu.MenuAction("Get Cookies", get_cookies)],
        ),
    ]
    webview.start(
        user_agent=user_agent,
        private_mode=False,
        storage_path=storage_path,
        gui="edgechromium",
        debug=True,
        menu=menu,
    )
    return _cookies
