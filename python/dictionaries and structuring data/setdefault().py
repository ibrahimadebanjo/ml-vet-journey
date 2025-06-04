# instead of this
spam = {"name" : "Ibrahim", "age" : 13}
if "color" not in spam.keys() :
    spam["color"] = "army-green"
#use this
print(spam)
spam = {"name" : "Ibrahim", "age" : 13}
if "color" not in spam.keys() :
    spam.setdefault("color", "army-green"  ) 
print(spam)     
#If the key does exist, the setdefault() method returns the key’s value.
print(spam.setdefault("color", "red"))