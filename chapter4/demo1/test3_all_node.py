from lxml import etree

html = etree.parse("./test.html",etree.HTMLParser())
# result = html.xpath("//*")
result = html.xpath("//li")
print(result)