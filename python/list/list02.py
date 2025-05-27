spam = [1,2,3,4] + ["A","B","C","D"]
print(spam)
spam = [1,2,3,4,5] * 3
print(spam)
spam = ["A","B","C","D"] * 3
print(spam)
del spam[2]
print(spam)
del spam
print(spam) #NameError
