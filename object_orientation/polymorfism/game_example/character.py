from abc import ABC, abstractmethod
from random import randint

class Character(ABC):
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
class PlayableCharacter(Character, ABC):
    
    @property
    @abstractmethod
    def stats(self): pass
    
    @abstractmethod
    def attack(self): pass
    
    @abstractmethod
    def heal(self): pass
    
    
class Warrior(PlayableCharacter):
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self.strength = randint(1, 10)
        
    @property
    def stats(self):
        return {"strength": self.strength}
    
    def attack(self):
        return self.strength * 2
    
    def heal(self):
        pass
    
class Mage(PlayableCharacter):

    def __init__(self, name, level):
        super().__init__(name, level)
        self.magic = randint(1, 10)

    @property
    def stats(self):
        return {"magic": self.magic}

    def attack(self):
        return self.magic

    def heal(self):
        return self.magic * 1.5
    
    
warrior = Warrior("Joe", 5)
mage = Mage("Kan", 8)

players = [warrior, mage]

for player in players:
    print(player.name, player.level, player.attack(), player.heal())