def print_params(a=5, b='Hello', c=False):
    print(a, b, c)


print_params()  # print_params с аргументами без переопределения выдаёт ошибку и на вход должно подаваться равное количество параметров
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'string', True]
values_dict = {'a': 15, 'b': 'goodbye', 'c': False}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [150, 'last chance']
print_params(*values_list_2, 42)