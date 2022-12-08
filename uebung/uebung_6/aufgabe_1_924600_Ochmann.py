"""Aufgabe 1"""

import math
class Point:
    def __init__(self, x, y):
        self.x= x
        self.y= y
    
    def __eq__(self, p):
        return (self.x==p.x) and (self.y==p.y)
    
    def center_distance(self):
        return math.sqrt(self.x**2+self.y**2)
class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius=radius

    def __eq__(self, p):
        return (self.x == p.x) and (self.y == p.y) and (self.radius == p.radius)


        

"""Ausgabem Beispiel"""
a=Circle(5, -3, 2.5)
b=Circle(5, -3, 2.5)
print(a==b)  # => True

a=Circle(5, -3, 2.5)
b=Circle(5, -3, 25.0)
print(a==b)  # => False