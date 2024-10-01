class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model} ')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power} ')

    def get_color(self):
        print(f'Цвет: {self.__color} ')

    def print_info(self):
        print(f'Модель: {self.__model} ')
        print(f'Мощность двигателя: {self.__engine_power} ')
        print(f'Цвет: {self.__color} ')
        print(f'Владелец: {self.owner} ')

    def set_color(self, new_color):
        if str.lower(new_color) not in Vehicle.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {new_color}')
        self.__color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()