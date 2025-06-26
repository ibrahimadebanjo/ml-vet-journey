class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f" Hi, I am {self.name}")
 

person = Person("Ibrahim Adebanjo")
print(person.name)
print(person.talk())
person = Person("John Smith")