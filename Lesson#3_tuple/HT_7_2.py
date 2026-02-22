"""
Создайте кортеж из 5 случайных чисел от 1 до 10. Все числа, кроме первого и
последнего, распаковать в один список. Для распаковки используйте *
"""

from random import randint


some_tuple = tuple(randint(1, 10) for _ in range(5))

_, *some_list, _ = some_tuple

print(some_list)

