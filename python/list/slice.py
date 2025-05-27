# Slice method in list
spam = ["cats", "Dogs", "elephants", "Lions"]
print(spam[1:3])
print(spam[0:4])
print(spam[1:-2])
print(spam[1:-1])
print(spam[1:])
print(spam[:3])
# length in list using len()
print(len(spam))
# chanigng value names with indexes 
spam[2] = "Horses"
print(spam)
spam[3] = spam[2]
print(spam)
spam[0] = 2025
print(spam)