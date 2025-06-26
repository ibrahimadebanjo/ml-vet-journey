# Class
class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")
        
# Create new objects: an instance of class
point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 100
print(point2.x)
