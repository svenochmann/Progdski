import math
import turtle as t
#------------------------------------------------------------------------
#------------------------------------------------------------------------
class GeometricObject:
    def __init__(self, x=0, y=0) -> None:
        self.position = (x,y)
        
        pass        

    def move_to_position(self):
        t.pu()
        t.goto((self.position))
        t.pd()
        pass

#------------------------------------------------------------------------
#------------------------------------------------------------------------

class Square(GeometricObject):
    def __init__(self,size,x=0,y=0):
        self.position = (x,y)
        self.size = size
        self.starting_angle = 0
        super().__init__(x,y)       
        pass
    
    
    def set_starting_angle(self, starting_angle):
        self.starting_angle = starting_angle
        pass


    def draw(self):
        self.move_to_position()
        t.seth(self.starting_angle)
        t.fd(self.size)
        t.left(90)
        t.fd(self.size)
        t.left(90)
        t.fd(self.size)
        t.left(90)
        t.fd(self.size)
        
        pass

    def calculate_area(self):
        sq_area = self.size * self.size 
        print(f"Area of the Triangle:{sq_area:.2f}m^2")
        pass
        
    

#------------------------------------------------------------------------
#------------------------------------------------------------------------

    

class Rectangle(GeometricObject):
    def __init__(self,lenght, hight, x=0,y=0):
        self.position = (x,y)
        self.size = (lenght, hight)
        self.starting_angle= 0
        
        pass
    
    def set_starting_angle(self, starting_angle):
        self.starting_angle = starting_angle
        pass


    
    
    def draw(self):
        self.move_to_position()
        t.seth(self.starting_angle)
        t.fd(self.size[0])
        t.left(90)
        t.fd(self.size[1])
        t.left(90)
        t.fd(self.size[0])
        t.left(90)
        t.fd(self.size[1])
        
        pass
        
    def calculate_area(self):
        r_area = self.size[0] * self.size[1]
        print(f"Area of the Rectangle:{r_area:.2f}m^2")
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------

class Triangle(GeometricObject):
    def __init__(self,size, x=0, y=0):
        self.position = (x,y)
        self.size = size
        self.starting_angle = 0
        pass
    
    def set_starting_angle(self, starting_angle):
        self.starting_angle = starting_angle
        pass



    def draw(self):
        self.move_to_position()
        t.seth(self.starting_angle)
        t.fd(self.size)
        t.lt(120)
        t.fd(self.size)
        t.lt(120)
        t.fd(self.size)
        
        pass
        
    def calculate_area(self):
        h = (self.size * math.sqrt(3))/2
        t_area = self.size*h/2
        print(f"Area of the Triangle:{t_area:.2f}m^2")
        pass    
#------------------------------------------------------------------------
#------------------------------------------------------------------------
        
class RegularPolygon(GeometricObject):
    def __init__(self,size,corner, x=0,y=0):
        super().__init__(x,y)
        self.position = (x,y)
        self.size = size
        self.corner= corner
        self.starting_angle = 0
        self.angle= 360 / self.corner
        pass
    
    def set_starting_angle(self, starting_angle):
        self.starting_angle = starting_angle

    def draw(self):
            self.move_to_position()
            t.seth(self.starting_angle)
            for _ in range(self.corner):
                t.fd(self.size)
                t.lt(self.angle)
            pass

    def calculate_area(self):
        
        p_area = self.corner*(self.size**2)/(4*math.tan(math.pi/self.corner))
        print(f"Area of the Polygon:{p_area:.2f}m^2")
        pass    

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def main():
    # ----- IGNORE THIS PART ---------------------------------
    wn = t.Screen()
    rootwindow = wn.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    # ----- IGNORE THIS PART ---------------------------------
    
    
    # AUFGABE 2.2 CODING COMES HERE
    
    #Square
    
    #1st: size 2nd: pos1 default = 0 3rd:pos2 default = 0
    
    sq = Square(100, 0, 0,)
    sq.draw()
    sq.calculate_area()
    
    #Rectangle
    # 1st: leanght 2nd: hight 4th: pos1 default  = 0 5th:pos2 deafault = 0
    
    rt = Rectangle(100, 50, 0, 0)
    rt.draw()
    rt.calculate_area()
    
    #Triangle
    # 1st: size 3rd:pos1 default =0 4th:pos2 default=0
    
    tr = Triangle(100, 0, 0)
    tr.draw()
    tr.calculate_area()
    
    #Regular Polygon
    #1st: lenght 2nd: corners 4th:pos1 default = 0 5th: pos2 default = 0:
    
    rp = RegularPolygon(100, 8, 0, 0)
    rp.draw()
    rp.calculate_area()
    
    
    
    #
    # ----- IGNORE THIS PART ---------------------------------
    wn.mainloop()
    t.done()
    # ----- IGNORE THIS PART ---------------------------------

main()