spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)
# different from list 
# list refrece is actually the value that points to the list
spam = ["hello", 2,7,0,4,2,"It's", "me"]
cheese = spam
cheese[-1] = "you"
print(cheese)
print(spam)