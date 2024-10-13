first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(first) - len(second) for first, second in zip(first, second) if len(first) != len(second)]
print(first_result)

second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]
print(second_result)