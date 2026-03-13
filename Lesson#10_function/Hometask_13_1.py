"""
Из полученного списка чисел создайте список с суммами
этих чисел, отсортированными по возрастанию
"""

input_numbers_list: list[int] = [int(number) for number in input("Введите числа через пробел: ").split()]


def sum_of_digits(numbers_list: list[int]) -> list[int]:
    return sorted([sum(map(int, str(number))) for number in numbers_list])


print(sum_of_digits(numbers_list=input_numbers_list))

