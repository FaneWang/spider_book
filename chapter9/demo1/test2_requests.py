import requests
# proxy = "125.70.13.77:8080"
proxy = "125.70.13.77:8080"
proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy
}

try:
    response = requests.get('https://www.baidu.com',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)    