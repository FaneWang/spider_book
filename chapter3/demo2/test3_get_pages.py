import requests
import re
from pyquery import PyQuery as pq

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# r = requests.get("https://www.zhihu.com/explore", headers=headers)
r = requests.get("http://www.66ip.cn/1.html", headers=headers)
# pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>", re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
doc = pq(r.text)
print(doc)