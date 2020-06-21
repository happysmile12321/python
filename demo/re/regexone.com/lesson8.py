#!/usr/bin/env python
import re

# ?

# Another quantifier that is really common when matching and extracting text is the ? (question mark)

# This metacharacter allows you to match either zero or one of the preceding character or group.

# For example, the pattern ab?c will match either the strings "abc" or "ac" because the b is considered optional.

# \? if you want to match ? 

# Match	1 file found?	To be completed
# Match	2 files found?	To be completed
# Match	24 files found?	To be completed
# Skip	No files found.

	
	
	
 
s0="1 file found?"
s1="2 files found?"
s2="24 files found?"
s3="No files found."
s0 = s0 + s1 + s2 + s3

print(re.findall('\d+ files? found\?',s0))












