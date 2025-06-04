while True:
    age = input()
    if age.isdecimal():
        break
    print("Pls Enter a number for your age")

while True:
    print("Select a new password (letters and numbers only):")
    age = input()
    if age.isalnum():
        break
    print("Password can only have letters or numbers")

