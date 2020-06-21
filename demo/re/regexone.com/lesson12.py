#!/usr/bin/env python
import re

# Task	Text	Capture Groups	 
# Capture	Jan 1987	Jan 1987 1987	To be completed
# Capture	May 1969	May 1969 1969	To be completed
# Capture	Aug 2011	

s1="Jan 1987"
s2='May 1969'
s3="Aug 2011"

res1 = re.findall('(\w+\s(\d+))',s1)
res2 = re.findall('(\w+\s(\d+))',s2)
res3 = re.findall('(\w+\s(\d+))',s3)
print(res1)
print(res2)
print(res3)
