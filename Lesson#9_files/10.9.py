"""
Создать список чисел. Записать каждое нечетное число в файл
"""

odd_numbers_list: list[int] = [int(number) for number in input("Введите числа через пробел: ").split()
                               if int(number) % 2 == 1]

with open('numbers.txt', 'w') as file:
    for number in odd_numbers_list:
        file.write(str(number) + '\n')

