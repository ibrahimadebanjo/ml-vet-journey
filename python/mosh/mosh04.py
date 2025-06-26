name = input("User :")
def greet_user(name):
    print(f"Hi {name}")
    print("Welcome ")


print("start")
greet_user(name)
print("Finish")
# keyword argument
def greet_again(firstName, lastName):
    print(f"Hello {firstName} {lastName}")
    print("Welcome")
# Keyword Argument
greet_again(lastName = "Adebanjo" , firstName = "Ibrahim")
# Try and except
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
except ZeroDivisionError:
    print("Age cannot be Zero")    
except ValueError:
    print("Invalid Value")



