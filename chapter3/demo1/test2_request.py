from urllib import request, parse

url = "http://httpbin.org/post"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Host":
    "httpbin.org"
}

dicts = {"name": "Germey"}

data = bytes(parse.urlencode(dicts), encoding="utf8")
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))