"""
Вход: список чисел. Программа строит диаграмму из *
"""

numbers_list = [int(number) for number in input().split()]

for count_of_stars in numbers_list:
    print(count_of_stars * "*")

