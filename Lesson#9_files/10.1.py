"""
Создать список из 10 cлучайных чисел.
Записать в файл:
1.Количество элементов в
списке
2. Все элементы списка в одну
строку
Т.е. в файле должно быть 2
строки
"""

import random

numbers_list: list[int] = [random.randint(1, 10) for _ in range(10)]

with open('numbers.txt', 'w') as file:
    file.write(str(len(numbers_list)) + '\n')

    file.write(' '.join(map(str, numbers_list)))

