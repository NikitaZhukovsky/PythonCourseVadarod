"""
Создайте 2 кортежа с 10 случайными числами от -5 до 0. Объедините их и посчитайте
сколько раз в получившемся кортеже встретится 0
"""

from random import randint

first_tuple = tuple(randint(-5, 0) for _ in range(10))
second_tuple = tuple(randint(-5, 0) for _ in range(10))

print(f"Количество нулей: {(first_tuple + second_tuple).count(0)}")

