#%%

import math

class Polygon:
    
    def area(self):
        pass
    
    
class Triangle(Polygon):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height / 2
        
        
class Circle(Polygon):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
        

shapes = [
        Circle(2),
        Triangle(2, 3),
        Circle(4)
        ]

        
for shape in shapes:
    print(shape.area())
        
        
        
    