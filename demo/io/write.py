import os
with open('DATA') as f:
    while True:
        num = f.readline()
        if num == "":
            break
        print(f.readline()[:-1])
