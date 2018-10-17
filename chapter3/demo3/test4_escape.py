import re 

content = "(fane)www.onepig.com"

result = re.match("^\(fane\)\w{3}\..*\..*",content)
print(result)
print(result.group())