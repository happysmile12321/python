#!/usr/bin/env python
import re
# In some cases, we might know that there are specific characters that we don't want to match too, for example, we might only want to match phone numbers that are not from the area code 650.

# To represent this, we use a similar expression that excludes specific characters using the square brackets and the ^ (hat). For example, the pattern [^abc] will match any single character except for the letters a, b, or c.

s1="hog"
s2='dog'
s3="bog"
s1 = s1 + s2 + s3
res1 = re.findall('[^h]og',s1)
print(res1)
