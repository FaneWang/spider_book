from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

roxyHandler = ProxyHandler({
    "http": "http://127.0.0.1:8080",
    "http": "https://127.0.0.1:8181",
})

opener = build_opener(ProxyHandler)

try:
    response = opener.open("https://www.baidu.com")
    print(response.read().decode("utf-8"))
except URLError as e:
    print(e.reason)