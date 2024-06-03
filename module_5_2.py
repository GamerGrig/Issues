class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        floors = input('Сколько этажей? ')
        self.numberOfFloors = floors
        print(f'Теперь в этом доме {self.numberOfFloors} этажей.')


my_house = House(15)
print(my_house.numberOfFloors)
my_house.setNewNumberOfFloors(35)
