import re

content = "Hello 123 4567 World_this is a regex demo"
print(len(content))
# result = re.match("^Hello(\s\d\d\d\s)(\d{4})\s\w{10}",content)
result = re.match("^Hello.*demo$",content)
print(result)
print(result.group(0))
# print(result.group(1))
print(result.span())