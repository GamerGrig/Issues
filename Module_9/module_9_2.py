first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str_len) for str_len in first_strings if len(str_len) > 5]
print(first_result)

second_result = [(i, j) for i in first_strings for j in second_strings if len(j) == len(i)]
print(second_result)

third_result = {k: len(k) for k in first_strings + second_strings if len(k) % 2 == 0}
print(third_result)