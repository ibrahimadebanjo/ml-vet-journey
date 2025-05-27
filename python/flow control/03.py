age = int(input("How old are you?:"))
if age >= 18:
    print("You are an adult")
elif age < 0:
    print("You are Yet to be born!")
else :
    print("You are a child!")

# logical operators (and,or, not)
# 1. and 
temp = int(input("what's the temperature outside?"))
if temp >= 0 and temp <= 30 :
    print("the temperature is good today")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
elif not (temp < 0 or temp > 30) :
    print("The temperature is good today!")
else :
 print("go take a coffee")