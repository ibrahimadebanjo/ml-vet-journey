# Inheritance
class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    pass #pass means nothing

class Cat(Mammal):
    def annoy(self):
        print("Annoying Cat")
dog1 = Dog()
dog1.walk()
cat = Cat()
cat.annoy()

