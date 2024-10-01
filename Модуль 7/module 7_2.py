file_name = "file_name.txt"
strings = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']


def custom_write(file_name, strings):
    result = {}

    with open(file_name, 'w') as file:
        for i, string in enumerate(strings, start=1):
            byte_position = file.tell()
            file.write(string + '\n')
            result[(i, byte_position)] = string

    return result

result = custom_write(file_name, strings)
print(result)