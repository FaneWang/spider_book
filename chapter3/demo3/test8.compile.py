import re 

content = "2016-12-15 12:00"

pattern = re.compile("\d{2}:\d{2}")

result = re.search(pattern,content)
print(result.group())