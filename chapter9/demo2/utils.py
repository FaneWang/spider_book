import requests
from requests.exceptions import ConnectionError

base_headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br, sdch',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8'
}


def get_page(url, options={}):
    headers = dict(base_headers, **options)
    print('正在抓取,', url)
    try:
        res = requests.get(url, headers=headers)
        print('抓取成功', url, res.status_code)
        if res.status_code == 200:
            return res.text
    except ConnectionError:
        print('抓取失败', url)
        return None
