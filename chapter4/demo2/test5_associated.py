from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,"lxml")
# print(soup.p.children)
# print(soup.p.contents)
# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

# print()
# print(soup.p.parent)
# print()
# for item in soup.p.parents:
#     print(item)

print(soup.a.next_sibling)
print(soup.a.previous_sibling)
print(soup.a.next_sibling.string)
print(list(soup.a.next_siblings))
print(list(soup.a.previous_siblings))
print(list(soup.a.next_siblings)[1]["class"])