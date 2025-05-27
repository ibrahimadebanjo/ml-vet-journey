spam = ["hello", "world", "ibrahim", "owolabi"]
print(spam.index("world"))
# duplicates of values and the first one(value index) is returned
spam = ["ibrahim", "owolabi", "owolabi", "adebanjo"]
print(spam.index("owolabi"))
# insert() and append() method
spam = ["Dog", "Cat", "bee"]
spam.append("moose")
print(spam)
# insert() method allows insertion of values at specific indexes
spam.insert(2, "Horse")
print(spam)
# remove() method
spam.remove("moose")
print(spam)
spam.sort()
print(spam)
num = [2, 1, 5, 76, 8, 5, 4, 2, 7, 8]
num.sort()
print(num)
# sort in alphabetical order rather than in ASCII
spam.sort(key=str.lower)
print(spam)
