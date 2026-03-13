"""
Напишите функцию которая принимает на вход список целых чисел,
 удаляет из него все нечётные значения, а чётные нацело делит на два.
"""

input_numbers_list: list[int] = [int(number) for number in input("Введите числа через пробел: ").split()]


def process_numbers(numbers_list: list[int]) -> list[int]:

    result_list: list[int] = [number // 2 for number in numbers_list if number % 2 == 0]

    return result_list


print(process_numbers(numbers_list=input_numbers_list))

