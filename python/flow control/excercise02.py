# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is 
# stored in spam, and prints Greetings! if anything else is stored in spam
i = 0
for i in range(5):
    if i == 1:
        print("Hello" )
    elif i == 2:
        print("Howdy")
    else:
        print("Greetings!") 
    print(i)          
#deepseek correction 
# for while loop
spam = 0
while spam < 5:
    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")
    spam += 1
# for for loop
for i in range(5):
    if i == 1:
        print("Hello")
    elif i == 2:
        print("Howdy")
    else:
        print("Greetings!")