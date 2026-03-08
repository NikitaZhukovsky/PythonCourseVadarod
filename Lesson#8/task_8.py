"""
Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
my_dictionary = {'data1': 375, 'data2': 567, 'data3': 37, 'data4': 21}
"""

my_dictionary = {'data1': 375, 'data2': 567, 'data3': 37, 'data4': 21}

result = 1

for k, v in my_dictionary.items():
    result *= v

print(result)

