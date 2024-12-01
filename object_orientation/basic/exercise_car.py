# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name):
        self._name = name
        self._motor = None
        self._factory = None
    
    @property
    def name(self):
        return self._name

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, value):
        self._motor = value
        
    @property
    def factory(self):
        return self._factory
    
    @factory.setter
    def factory(self, value):
        self._factory = value        
    
class Motor:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
class Factory:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
fusca = Car('Fusca')
vw = Factory('VW')
motor_v8 = Motor('V8')

fusca.factory = vw
fusca.motor = motor_v8

print(fusca.name, fusca.motor.name, fusca.factory.name)

fiat = Car('Uno')
vw = Factory('Fiat')
motor_10 = Motor('1.0')

fiat.factory = vw
fiat.motor = motor_10

print(fiat.name, fiat.motor.name, fiat.factory.name)

    