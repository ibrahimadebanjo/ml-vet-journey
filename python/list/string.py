name = "Ibrahim"
print(name)
print(name[0])
# strings are immutable
# name[0] = "hello"
print(type(("hello")))
print(type(("hello",)))

name = ["cat","dog","goat"]
tup = ("hello", "world")
# converting tuple to list with list() and tupple() function and vise versa
print (list(tup))
print (tuple(name))