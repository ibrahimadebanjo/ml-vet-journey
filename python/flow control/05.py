# not operator 
print(not True) #False
print(not False) #True
# or operator
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False)#False
# and operator
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
# multiple boolean operators
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
# if statement 
name = input()
if name == name :
    print("hello" + name)
else : 
    print("null") 

age = int(input())      
if age < 10 :
    print("Youre still a kid")    
elif age <  18 or age > 10: 
    print("you are a teenager")
else : 
    print("You're an Adult")    
