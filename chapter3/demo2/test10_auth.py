import requests
from requests.auth import HTTPBasicAuth

# r = requests.get("http://www.onepig.top",auth=HTTPBasicAuth("2079409377@qq.com","happywyf==1314"))
r = requests.get("http://www.onepig.top",auth=("2079409377@qq.com","happywyf==1314"))

print(r.status_code)