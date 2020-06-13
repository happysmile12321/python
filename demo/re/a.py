import re

a='Apple Do not eat 123 dollars.Please.456,789'

#patten='[0-9]+'

patten='[_A-Za-z]+'


res=re.findall(patten,a)

print(res)
