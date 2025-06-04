birthdays = {"Alice" : "Jan 02", "Bob" : "April 10", "Abeedah" : "Nov 20", "Muhammad" : "June 25"}

while True:
    print("Enter Your Name")
    name = input()
    if name == " ":
        break
    if name in birthdays:
        print( birthdays[name] + "is the birthday of " + name)
    else:
        print("I dont have information for birthday" + name)
        print("What is Their Birthday?")
        baby = input()
        birthdays[name] = baby
        print("Birthday Database Updated")
