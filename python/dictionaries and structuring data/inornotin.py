spam = {"name": "Ibrahim", "age": "22"}
print("name" in spam.keys())  # True
print(22 in spam.values())
print("Owolabi" in spam.values())
print("Ibrahim" in spam.values())
print("Ibrahim" not in spam.values())
print("age" not in spam.values())
print("At-taariq" not in spam.values())
print("color" in spam)
print("color" not in spam)
#  notice that 'color' in spam is essentially a shorter version of writing 'color' in spam.keys().
