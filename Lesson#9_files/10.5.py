"""
Создать множество отрицательных и положительных чисел.
Записать его в файл построчно.
"""

import random

numbers_set: set[int] = {random.randint(-10, 10) for _ in range(10)}

with open('numbers.txt', 'w') as file:
    for num in sorted(numbers_set):
        file.write(str(num) + "\n")

