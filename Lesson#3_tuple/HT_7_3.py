"""
На вход программе подаются числа. Создайте кортеж из чисел меньше 5.
"""

numbers = tuple(map(int, input("Введите числа через пробел: ").split()))

result = tuple(number for number in numbers if number < 5)

print(result)

