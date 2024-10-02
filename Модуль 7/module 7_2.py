file_name = 'file_name.txt'

strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    positions = {}
    with open(file_name, 'w', encoding='utf-8') as fs:
        for i in range(len(strings)):
            pos = fs.tell()
            fs.write(strings[i] + '\n')
            positions[i + 1, pos] = strings[i]

    return positions
