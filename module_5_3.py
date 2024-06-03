class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors


building_1 = Building(150, 'Небоскрёб')
building_2 = Building(15, 'Хрущовка')
print(building_1 == building_2)