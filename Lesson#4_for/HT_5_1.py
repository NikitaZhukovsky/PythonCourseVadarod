"""
Программа перемножает все нечетные значения от 1 до 10 включительно
"""

numbers_list = [number for number in range(1, 11) if number % 2 == 1]

result = 1

for number in numbers_list:
    result *= number

print(result)

