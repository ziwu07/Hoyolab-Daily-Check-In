from http.cookies import SimpleCookie
import os, webview, webview.menu

storage_path = os.path.join(os.getcwd(), "webview_storage")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


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
        webview.menu.Menu("Actions", [
            webview.menu.MenuAction("Get Cookies", get_cookies),
            webview.menu.MenuAction("Quit", quit),
        ])
    ]
    webview.start(
        user_agent=user_agent,
        private_mode=False,
        storage_path=storage_path,
        gui="qt",
        menu=menu,
    )
    return _cookies
