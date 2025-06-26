# Class
class Point:
    # self seen is a refernce to the current object
    # This method is known as constructor
    def __init__(self, x, y ):
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")
        
# Create new objects: an instance of class
point1 = Point(11,20)# representing x and y coordinates
# Constructor: it is a function called  at the time of creating a object
print(point1.x)
