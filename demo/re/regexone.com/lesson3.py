#!/usr/bin/env python


# There is a method for matching specific characters using regular expressions, by defining them inside square brackets
# For example, the pattern [abc] will only match a single a, b, or c letter and nothing else.

# start
# Below are a couple lines, where we only want to match the first three strings, but not the last three strings.
# Notice how we can't avoid matching the last three strings if we use the dot, but have to specifically define what letters to match using the notation above.



import re


# Match	can	
# Match	man	
# Match	fan	
# Skip	dan	
# Skip	ran	
# Skip	pan

s1 = "can\n"
s2 = "man\n"
s3 = "fan\n"
s4 = "dan\n"
s5 = "ran\n"
s6 = "pan\n"

s1 = s1+s2+s3+s4+s5+s6

res1 = re.findall('[cmf]an',s1)
print(res1)
