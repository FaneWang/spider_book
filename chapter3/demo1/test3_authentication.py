from urllib.error import URLError
from urllib.request import (HTTPBasicAuthHandler,
                            HTTPPasswordMgrWithDefaultRealm, build_opener)

log = "username"
pwd = "password"
url = "http://www.onepig.top/wp-login.php"

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, log, pwd)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
