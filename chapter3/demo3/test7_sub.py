import re 

content = 'fegr545grgr454gr4546356gr'

content = re.sub("\d","f",content)
print(content)