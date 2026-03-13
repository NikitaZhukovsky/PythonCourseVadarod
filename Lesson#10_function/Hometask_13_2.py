"""
Напишите функцию f(x), которая возвращает значение следующей функции,
определённой на всей числовой прямой:
"""

number: float = float(input("Введите число: "))


def f(x) -> float:
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif x <= 2:
        return -x / 2
    else:
        return (x - 2) ** 2 + 1


print(f(x=number))
