#!/usr/bin/env python
import re

# *
# .* can patterm any long char

# Exercise 7: Matching Repeated Characters
# Task	Text	 
# Match	aaaabcc	To be completed
# Match	aabbbbc	To be completed
# Match	aacc	To be completed
# Skip	a

s0="aaaabcc"
s1="aabbbbc"
s2="aacc"
s3="a"
s0 = s0 + s1 + s2 + s3 

print(re.findall('a{2}[ab]*c+',s0))
