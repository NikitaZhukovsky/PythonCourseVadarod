"""
Определите сумму элементов, кратных 5, последовательности, заканчивающейся
числом 0.
"""

numbers_list = [int(number) for number in input().split()]
sum_of_numbers = 0
i = 0

while i < len(numbers_list):
    if numbers_list[i] % 10 == 0:
        sum_of_numbers += numbers_list[i]
    i += 1

print(sum_of_numbers)

