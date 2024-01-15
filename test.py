from http.cookies import SimpleCookie
import http.cookiejar
import _webview
import os

class FakeRequest:
    def __init__(self, url, host, unverifiable, origin_req_host):
        self.host = host,
        self.unverifiable = unverifiable
        self.origin_req_host = origin_req_host
        self.url = url
    
    def get_full_url(self):
        return self.url
    
class FakeResponse:
    def __init__(self):
        
        
    def info(self):
        
class FakeMessage:
    def __init__(self) -> None:
        
    def get_all(self):
        self.headers

cookie = _webview.lauch_webview("https://www.google.com")
cookies = http.cookiejar.CookieJar()
headers = "Set-Cookie:"
print(type(cookie))
for c in cookie:
    as_str = c.output(header=headers)
    cookies.extract_cookies
