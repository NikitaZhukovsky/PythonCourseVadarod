"""
Создайте кортеж из 10 случайных чисел от 1 до 20.
Найдите количество уникальных чисел, сумму всех чисел и индекс максимального элемента
"""
from random import randint


numbers = tuple(randint(1, 20) for _ in range(10))


print(f"Кортеж: {numbers}\n"
      f"Количество уникальных чисел: {len(set(numbers))}\n"
      f"Cумма всех чисел: {sum(numbers)}\n"
      f"Индекс максимального элемента: {numbers.index(max(numbers))}")

