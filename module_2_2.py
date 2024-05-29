first = 12
second = 123
third = 123
if first == second == third:
    print(3)
elif first == second or first == third:
    print(2)
elif second == first or second == third:
    print(2)
elif third == first or third == second:
    print(2)
else:
    print(0)