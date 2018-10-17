import requests

r = requests.get("http://www.onepig.top")
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)