#!/usr/bin/env python

# In this case, the character \d can be used in place of any digit from 0 to 9. 
# The preceding slash distinguishes it from the simple d character and indicates that it is a metacharacter.


import re
s1="abc123xyz"
s2='define "123"'
s3="var g = 123;"

res1 = re.findall('\d\d\d',s1)
res2 = re.findall('\d',s2)
res3 = re.findall('\d',s3)
print(res1)
print(res2)
print(res3)
