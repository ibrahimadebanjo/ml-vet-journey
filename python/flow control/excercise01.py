while True:
    print("What's Your name ?")
    name = input()
    if name != "Joe" :
        continue
    print("Hello, Joe. What's your password?")
    password = input()
    if password != "swordfish":
        continue
    print("Access granted!")

