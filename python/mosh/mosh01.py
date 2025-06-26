print("*" * 10)
# Formatted string
first = "Ibrahim"
last = "Adebanjo"
message = first + " [" + last + "]" + " is a Machine Learning Engineer"
msg = f"{first} [{last} ] is a Machine Learning Engineer"
print(message)
print(msg)
# Order of operation
"""
Parenthesis
exponentiation 2 ** 3
multiplication or division
addition or subtraction
"""
print(10 + 3 * 2 ** 2)
print((10 + 3) * 2 ** 2)

# While loop
i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")
# Guess game
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess :"))
    guess_count += 1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("You Lose")
''''
The else is at hte level of while loop because if the user 
input is True it returns You won and breaks out of the loop
but if it is false the loop will run three times and then proceed
to else statement, printing you lose
Remember : Python excecutes code line by line
'''