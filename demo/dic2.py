phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)



for name,phone in phonebook.items():
    print("key:%s -- value:%d"%(name,phone))
del phonebook["Jill"]
print("---")
for name,phone in phonebook.items():
    print("key:%s -- value:%d"%(name,phone))
phonebook.pop("Jack")
print("---")
for name,phone in phonebook.items():
    print("key:%s -- value:%d"%(name,phone))
print("---")
phonebook["Bob"]=123223443432
phonebook["Jake"]=938273443
for name,phone in phonebook.items():
    print("key:%s -- value:%d"%(name,phone))
