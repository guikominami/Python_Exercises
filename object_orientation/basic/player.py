import os

class Person:
    def __init__(self, name, surname, type_class, power, defense):
        self.name = name
        self.surname = surname
        self.typeclass = type_class
        self.power = power
        self.defense = defense

os.system('cls')

p1 = Person('Gui', 'Kominami', 'gnomo careca', 10, 20)
print(p1.name, p1.surname, p1.typeclass, p1.power, p1.defense)


