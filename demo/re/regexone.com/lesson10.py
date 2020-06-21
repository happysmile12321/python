#!/usr/bin/env python
import re

# ^success to match only a line that begins with the word "success", but not the line "Error: unsuccessful operation"

#　Note that this is different than the hat used inside a set of bracket [^...] for excluding characters, which can be confusing when reading regular expressions.




#　Task	Text	 
#　Match	Mission: successful	To be completed
#　Skip	Last Mission: unsuccessful	To be completed
#　Skip	Next Mission: successful upon capture of target


s0="Mission: successful"
s1="Last Mission: unsuccessful"
s2="Next Mission: successful"
s0 = s0 + s1 + s2

# don't support?
print(re.findall('^Mission: successful$',s0))
