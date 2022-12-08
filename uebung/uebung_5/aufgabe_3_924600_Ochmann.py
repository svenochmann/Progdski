"""Aufgabe 3"""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def position(self):
        print(self.x, self.y)
    def center_distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
   



class Circle(Point):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.center = Point(self.x, self.y)
        
        
        
    
       

circle_1 = Circle(x=2, y=3.5, radius=5.5)

print(circle_1.radius)  # --> 5.5

circle_1.center.position()
 

 #center.position()  # --> 2 3.5