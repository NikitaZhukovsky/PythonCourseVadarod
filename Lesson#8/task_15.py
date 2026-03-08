"""
Список из случайных 10 чисел. Найти их сумму и произведение.
"""

import random

numbers_list = [random.randint(1, 10) for i in range(10)]

result = 1

for number in numbers_list:
    result *= number

print(f"Сумма: {sum(numbers_list)}")
print(f"Произведение: {result}")

