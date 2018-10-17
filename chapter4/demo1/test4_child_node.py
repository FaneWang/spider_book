from lxml import etree

html = etree.parse("./test",etree.HTMLParser())
result = html.xpath("//li/a")
print(result)