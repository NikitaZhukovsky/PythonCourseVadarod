"""
Определите кол-во отрицательных и положительных элементов последовательности,
заканчивающейся числом 0.
"""

numbers_list = [int(number) for number in input().split()]
positive_count = 0
negative_count = 0

for number in numbers_list:
    if number % 10 == 0:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

print(f"Число положительных элементов: {positive_count}, число отрицательных: {negative_count}")

