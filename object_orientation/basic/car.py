class Car:
    def __init__(self, name):
        self.name = name

    def acelerate(self):
        print(f'{self.name} is acelerating!')   

fusca = Car('Fusca')
fusca.acelerate()        