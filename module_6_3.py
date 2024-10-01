class Vehile:
    def __init__(self):
        self.vehile_type = None

class Car:
    def __init__(self, power):
        self.price = 1000000
        self.power = power


    def horse_powers(self):
       return self.power

class Nissan(Car, Vehile):
    def __init__(self, power):
        super().__init__(power)
        self.price = 200000
        self.vehile_type = 'Sedan'

    def horse_powers(self):
        print(f'Power Nissan {self.power}')

car = Nissan(150)

print(car.horse_powers(), car.price, car.vehile_type)