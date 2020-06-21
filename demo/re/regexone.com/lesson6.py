#!/usr/bin/env python
import re

#  \d\d\d which would match exactly three digits.

# A more convenient way is to specify how many repetitions of each character we want using the curly braces notation.
# a{3} will match the a character exactly three times.

# Certain regular expression engines will even allow you to specify a range for this repetition such that a{1,3} will match the a character no more than 3 times, but no less than once for example.

# w{3} (three w's)
# [wxy]{5} (five characters, each of which can be a w, x, or y) 
# .{2,6} (between two and six of any character).


# Task	Text	 
# Match	wazzzzzup	To be completed
# Match	wazzzup	To be completed
# Skip	wazup	To be completed


s0 = "Text"+"wazzzzzup"+"wazzzup"+"wazup"

# 找到所有大写字母，后面跟3个字母
print(re.findall('[A-Z].{3}',s0))
# 找到所有以z开始的然后后面跟2个
print(re.findall('[z].{2}',s0))
# 找到3个z
print(re.findall('z{3}',s0))

# Answer
print(re.findall('waz{2,4}.',s0))

