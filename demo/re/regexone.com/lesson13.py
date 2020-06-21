#!/usr/bin/env python
import re



# Task	Text	Capture Groups	 
# Capture	1280x720	1280 720	Failed
# Capture	1920x1600	1920 1600	Failed
# Capture	1024x768	1024 768





s1="1280x720"
s2='1920x1600'
s3="1024x768"

res1 = re.findall('(\d+)x(\d+)',s1)
res2 = re.findall('(\d+)x(\d+)',s2)
res3 = re.findall('(\d+)x(\d+)',s3)
print(res1)
print(res2)
print(res3)
