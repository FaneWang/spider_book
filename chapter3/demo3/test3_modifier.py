# .匹配除换行符之外的所有字符，加上re.S可以匹配换行符，还有其他的修饰符

import re 
content = '''Hello 1234567 World_This 
is a Regex Demo'''

result = re.match("^He.*?(\d+).*Demo$",content,re.S)
print(result)
print(result.group(1))