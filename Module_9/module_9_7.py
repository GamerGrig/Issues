def is_prime(func):
    def wrapper(*args, **kwargs):
        original = func(*args, **kwargs)
        if original <= 1:
            return f'Составное число\n{original}'
        for i in range(2, int(original ** 0.5) + 1):
            if original % i == 0:
                return f'Составное число\n{original}'
        return f'Простое число\n{original}'
    return wrapper


@is_prime
def sum_tree(a, b, c):
    res = a + b + c
    return res


# Простое число
result = sum_tree(2, 3, 6)
print(result)
# Составное число
result = sum_tree(3, 3, 6)
print(result)