class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            for i in range(1, self.number_of_floors + 1):
                print(i)
            print('Такого этажа не существует!')
        elif new_floor < self.number_of_floors - self.number_of_floors:
            print('У меня подвала нет вообще-то..')
        else:
            for i in range(1, new_floor + 1):
                print(i)


my_house = House('Мой дом', 5)
my_house.go_to(-4)
