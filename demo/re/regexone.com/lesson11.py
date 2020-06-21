#!/usr/bin/env python
import re

# define group
# Regular expressions allow us to not just match text but also to extract information for "further processing.!!!" 
#  ( and ) 

# Imagine for example that you had a command line tool to list all the image files you have in the cloud. 
# you can ^(IMG\d+\.png)$ 

# but if you only wanted to capture the filename without the extension,
# ^(IMG\d+)\.png$ 
# only captures the part before the period.


# Task	Text	Capture Groups	 
# Capture	file_record_transcript.pdf	file_record_transcript	To be completed
# Capture	file_07241999.pdf	file_07241999	To be completed
# Skip	testfile_fake.pdf.tmp


s1="file_record_transcript.pdf"
s2="file_07241999.pdf"
s3="testfile_fake.pdf.tmp"


res1 = re.findall('^(file.+)\.pdf$',s1)
res2 = re.findall('^(file.+)\.pdf$',s2)
res3 = re.findall('^(file.+)\.pdf$',s3)
print(res1)
print(res2)
print(res3)
