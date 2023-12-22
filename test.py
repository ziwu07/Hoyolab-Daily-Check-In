from http.cookiejar import CookieJar
import api_calls
from main import genshin_ref_url, genshin_req_url


print(api_calls.api_call(genshin_req_url, genshin_ref_url, cookie=CookieJar()))
