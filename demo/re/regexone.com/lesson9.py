#!/usr/bin/env python
import re

# \s == whitespace

# The most common forms of whitespace you will use with regular expressions are the space (␣), the tab (\t), the new line (\n) and the carriage return (\r) (useful in Windows environments), and these special characters match each of their respective whitespaces. In addition, a whitespace special character \s will match any of the specific whitespaces above and is extremely useful when dealing with raw input text.


# Task	Text	 
# Match	1.   abc	To be completed
# Match	2.	abc	To be completed
# Match	3.           abc	To be completed
# Skip	4.abc


s0="1.   abc"
s1="2.	abc"	
s2="3.           abc"
s3="4.abc"

s0 = s0 + s1 + s2 + s3

#print(re.findall('\d \s+ ab?',s0))
print(re.findall('\d\.\s+abc?',s0))
