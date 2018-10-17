# 贪婪匹配尽可能多的匹配，非贪婪匹配尽可能少的匹配

import re 

content = "Hello 1234567 World_This is a Regex Demo"
# 贪婪模式，尽可能多的匹配数字
# result = re.match("^He.*(\d+).*Demo$",content)
# 非贪婪模式，尽可能少的匹配数字，不要在结尾使用
result = re.match("^He.*?(\d+).*Demo$",content)
print(result)
print(result.group(1))