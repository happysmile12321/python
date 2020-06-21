#!/usr/bin/env python
import re

# the pattern [0-6] will only match any single digit character from zero to six, and nothing else.
# And likewise, [^n-p] will only match any single character except for letters n to p.

# An example of this is the alphanumeric \w metacharacter which is equivalent to the character range [A-Za-z0-9_] and often used to match characters in English text.


# Task	Text	 
# Match	Ana	To be completed
# Match	Bob	To be completed
# Match	Cpc	To be completed
# Skip	aax	To be completed
# Skip	bby	To be completed
# Skip	ccz


s0="Ana"
s1="Bob"
s2="Cpc"
s3="aax"
s4="bby"
s5="ccz"
s0 = s0 + s1 + s2 + s3 + s4 + s5

print(re.findall('[^a-z]..',s0))
