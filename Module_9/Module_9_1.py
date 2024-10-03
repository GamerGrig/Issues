def apply_all_func(int_list: list, *functions):
    reults = {}
    for i in functions:
        reults[i.__name__] = i(int_list)
    return reults


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))