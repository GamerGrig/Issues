from random import randint

rock_1 = randint(3, 20)
print(rock_1)
result = []

for i in range(1, rock_1 + 1):
    for k in range(i + 1, rock_1 + 1):
        if rock_1 % (i + k) == 0:
            result.append((i, k))

print(*result)
