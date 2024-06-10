class Car:

    def horse_powers(self):
        horse_powers = self.horse_powers

    price = 100000
    horse_powers = 280


class Nissan(Car):
    price = 5000000
    horse_powers = 300


class Kia(Car):
    price = 3000000
    horse_powers = 290


car_1 = Car()
car_2 = Nissan()
car_3 = Kia()
print(car_1.price, car_1.horse_powers)
print(car_2.price, car_2.horse_powers)
print(car_3.price, car_3.horse_powers)
