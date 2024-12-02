from abc import ABC, abstractmethod
from math import pi

#-------------------------------------------------------------------------------------
# Abstração: A classe forma é uma classe abstrata, que possui uma área e um perímetro
#-------------------------------------------------------------------------------------
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
#-------------------------------------------------------------------------------------
# Herança: Os objetos quadrado e círculo herdam a classe Forma
#-------------------------------------------------------------------------------------
class Square(Shape):
    
    def __init__(self, side):
        self.side = side
        
    #-------------------------------------------------------------------------------------
    # Polimorfismo: Os objetos da mesma classe possuem comportamentos diferentes.
    # A área e o perímetro de um quadrado são calculados de maneira diferente do círculo
    #-------------------------------------------------------------------------------------        
        
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
    
if __name__ == "__main__":
    
    s1 = Square(2)
    c1 = Circle(2)

    shapes = [s1, c1]

    for shape in shapes:
        print(shape.area())
        print(shape.perimeter())