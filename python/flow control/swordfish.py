while True:
    print("What's Your name?")
    name = input()
    if name != "Joe" :
        continue
    print("Hello " + name + " what is Your password?")
    password = input()
    if password == "swordfish":
        break
    print("access granted!")

