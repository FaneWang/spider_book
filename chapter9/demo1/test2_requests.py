import requests
proxy = "125.70.13.77:8080"
proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy
}

try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)    