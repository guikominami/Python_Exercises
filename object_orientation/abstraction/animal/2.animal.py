# class Animal
# class Lion(Animal)
#   feed
# class Panda(Animal)
#   feed
# class Snake(Animal)
#   feed

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod  # Decorator to define an abstract method  
    def feed(self):
        pass    
    
class Lion(Animal):
    def feed(self):
        print("Feeding a lion with raw meat!")
    
class Panda(Animal):
    def feed(self):
        print("Feeding a panda with some tasty bamboo!")
    
class Lion(Animal):
    def feed(self):
        print("Feeding a snake with mice!")
    
l = Lion()
l.feed()