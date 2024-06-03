class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for i in range(40):
    house = Building()
    print(Building.total)