"""
На вход подается список чисел. Создать словарь, в котором ключ — число, значение —
число на 10% больше. Значение должно быть округленное.
"""

numbers_list = [int(number) for number in input("Введите целые числа через пробел: ").split()]

numbers_dict = {number: round(number * 1.1, 1) for number in numbers_list}

print(numbers_dict)

