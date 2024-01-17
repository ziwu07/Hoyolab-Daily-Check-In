from config import LOGIN_URI
import cookies, api_calls
from main import genshin_ref_url, genshin_req_url


cookie = cookies.get_cookies(LOGIN_URI)
print(api_calls.claim(req_url=genshin_req_url, ref_url=genshin_ref_url, cookie=cookie))
