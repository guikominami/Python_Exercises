import os

class Person:
    def __init__(self, name, surname, type_class, power, defense):
        self.name = name
        self.surname = surname

os.system('cls')

p1 = Person('Gui', 'Kominami')
print(p1.name, p1.surname)


