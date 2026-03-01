"""
Числа 1, 1, 2, 3, 5, 8 … являются частью последовательности Фибоначчи.
Каждое число в последовательности, после первых двух является суммой двух предыдущих чисел последовательности.
Напишите программу, которая вычисляет и выводит на экран n-ое число последовательности.
Число n вводиться с клавиатуры.
"""

n = int(input("Введите номер числа Фибоначчи: "))

if n == 1 or n == 2:
    print(1)
else:
    first_number, second_number = 1, 1
    count = 2

    while count < n:
        first_number, second_number = second_number, first_number + second_number
        count += 1

    print(second_number)

