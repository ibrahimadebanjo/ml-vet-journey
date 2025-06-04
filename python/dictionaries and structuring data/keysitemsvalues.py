# The keys(), values(), and items() Methods
spam = {"Color": "green", "Name": "Ibrahim", "Nickname": "At-taariq"}
for i in spam.keys():
    print(i)

for i in spam.values():
    print(i)

for i in spam.items():
    print(i)
print(spam.keys())
print(list(spam.keys()))
spam = {"Color": "green", "Name": "Ibrahim", "Nickname": "At-taariq", "age" : 22}
for k, v in spam.items():
    print("Key :" + k + " Value :" + str(v))
