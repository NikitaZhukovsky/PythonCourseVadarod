"""
Напишите функцию, которая создает список случайных элементов. На вход функция
принимает кол-во элементов, минимальное и максимальное значение
"""

import random


def rand_nums(count_of_numbers: int, min_value: int, max_value: int) -> list[int]:
    return [random.randint(min_value, max_value) for _ in range(count_of_numbers)]


print(rand_nums(count_of_numbers=7, min_value=2, max_value=12))

