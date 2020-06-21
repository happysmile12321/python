#!/usr/bin/env python
import re

# |

# Specifically when using groups, you can use the | (logical OR, aka. the pipe) to denote different possible sets of characters. 

# In the above example, I can write the pattern "Buy more (milk|bread|juice)" to match only the strings Buy more milk, Buy more bread, or Buy more juice.


# Task	Text	 
# Match	I love cats	To be completed
# Match	I love dogs	To be completed
# Skip	I love logs	To be completed
# Skip	I love cogs

s1="I love cats"
s2='I love dogs'
s3="I love logs"
s4="I love cogs"
s1 = s1+s2+s3+s4
res1 = re.findall('I love (cats|dogs)',s1)
print(res1)
