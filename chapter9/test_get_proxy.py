import requests

PROXY_POOL_GET_URL = "http://127.0.0.1:8888/random"
PROXY_POOL_COUNT_URL = "http://127.0.0.1:8888/count"


def get_proxy():
    try:
        res = requests.get(PROXY_POOL_GET_URL)
        if res.status_code == 200:
            return res.text
    except ConnectionError:
        return None


def get_proxy_count():
    try:
        res = requests.get(PROXY_POOL_COUNT_URL)
        if res.status_code == 200:
            return res.text
    except ConnectionError:
        return None


if __name__ == "__main__":
    print(get_proxy())
    print('-------------------------------------------------------------------------------')
    print(get_proxy_count())
