from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Square(Shape):
    
    def __init__(self, side):
        self.side = side
        
    # (**) square
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    # (**) square
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius    