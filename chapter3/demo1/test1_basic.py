import urllib.request
import urllib.parse
import socket
import urllib.error

data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding="utf8")
try:
    response = urllib.request.urlopen(
        "http://httpbin.org/post", data=data, timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("Time out")
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))
# print(response.read())