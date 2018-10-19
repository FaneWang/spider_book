# same as codes shown in the following
# from pyquery import PyQuery as pq

# doc = pq(url="http://www.onepig.top")
# print(doc("title"))

from pyquery import PyQuery as pq
import requests

# doc = pq(requests.get("http://www.onepig.top").text)
# print(doc("title"))

# initialize using files
doc = pq(filename="test.html")
print(doc("li"))