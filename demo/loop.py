c = 0
while c <= 50:
    c += 1
    if c % 2 == 0:
        print(c)
        break
else:
    print("I am else")
c = 0
while c <= 50:
    c += 1
    if c % 2 == 0:
        print(c)
        continue
else:
    print("I am else")
print('$'*100)
c = 0
while c <= 50:
    c += 1
    if c % 2 == 0:
        print(c)
        continue
    else:
        print("I am odd")

