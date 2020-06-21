#!/usr/bin/env python
import re

# For example, \D represents any non-digit character, \S any non-whitespace character, and \W any non-alphanumeric character (such as punctuation). 


# Additionally, there is a special metacharacter \b which matches the boundary between a word and a non-word character.
#  It's most useful in capturing entire words (for example by using the pattern \w+\b).


# many systems allow you to reference your captured groups by using \0 (usually the full matched text), \1 (group 1), \2 (group 2), etc


# This is useful for example when you are in a text editor and doing a search and replace using regular expressions to swap two numbers, you can search for "(\d+)-(\d+)" and replace it with "\2-\1" to put the second captured number first, and the first captured number second for example.


# Task	Text	 
# Match	The quick brown fox jumps over the lazy dog.	To be completed
# Match	There were 614 instances of students getting 90.0% or above.	To be completed
# Match	The FCC had to censor the network for saying &$#*@!.	To be completed


s1="The quick brown fox jumps over the lazy dog."
s2="There were 614 instances of students getting 90.0% or above."
s3="The FCC had to censor the network for saying &$#*@!."

res1 = re.findall('.*',s1)
res2 = re.findall('.*',s2)
res3 = re.findall('.*',s3)
print(res1)
print(res2)
print(res3)
