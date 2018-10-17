import time

import requests

from test2 import writeToFile, parseOnePage


def getOnePage(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = getOnePage(url)
    # print(html)
    # parseOnePage(html)
    for item in parseOnePage(html):
        print(item)
        writeToFile(item)


if __name__ == "__main__":
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
