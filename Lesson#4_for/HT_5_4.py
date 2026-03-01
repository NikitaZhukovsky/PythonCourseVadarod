"""
Переписать задачи 5.4, 5.5., 5.7, чтобы на вход получался список с использованием
генератора списков
"""

# 5.4

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

numbers_list = [number for number in range(a, b + 1)]

print(numbers_list)


# 5.5
a = int(input("Введите a: "))
b = int(input("Введите b: "))

evens_numbers_list = [number for number in range(a, b + 1) if number % 2 == 0]

print(evens_numbers_list)


# 5.7
some_str = input("Введите строку: ")

double_chars = [char * 2 for char in some_str]
result = ''.join(double_chars)

print(result)

