from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy = '125.70.13.77:8080'
# proxy need verify
# proxy = 'usename:password@125.70.13.77:8080'
proxyHandler = ProxyHandler({
    'http':'http://' + proxy,
    'https':'https://' + proxy
})

opener = build_opener(proxyHandler)
try:
    response = opener.open("http://httpbin.org/get")
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)