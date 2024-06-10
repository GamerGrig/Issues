class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 0


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 200000

    def horse_powers(self):
        return f' horse powers {200}'


class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 3000000

    def horse_powers(self):
        return f' horse powers {300}'
