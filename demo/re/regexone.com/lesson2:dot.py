#!/usr/bin/env python
# 1. . can be a wildcard(. == any a char)
# Joker 
# In some card games, the Joker is a wildcard and can represent any card in the deck.
# With regular expressions, you are often matching pieces of text that you don't know the exact contents of

# 2. \. can skip a wildcard(any char)


import re
s1="cat."
s2="896."
s3="?=+."
s4="abc1"

res1 = re.findall('.',s1)
res5 = re.findall('\.',s1)
res2 = re.findall('.\d',s2)
res3 = re.findall('\.',s3)
res4 = re.findall('.',s4)
print(res1)
print(res5)
print(res2)
print(res3)
print(res4)
