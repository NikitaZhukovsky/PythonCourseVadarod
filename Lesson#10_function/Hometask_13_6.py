"""
Напишите функцию, вычисляющую значение факториала числа N.
Используйте рекурсию
"""


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(n=6))

