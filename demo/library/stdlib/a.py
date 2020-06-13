#/usr/bin/env python
import sys
# read a file
def readfile(filename):
    f = file(filename)
    while True:
        line = f.readline()
        if(len(len)==0):
            break
        print(line,)
        f.close()
readfile("TODO")
