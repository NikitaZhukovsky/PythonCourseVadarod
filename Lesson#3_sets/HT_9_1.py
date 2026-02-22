"""
На вход программа принимает 2 строки и выводит их общие символы.
"""

first_set = set(input("Введите первую строку: "))
second_set = set(input("Введите вторую строку: "))

print(first_set & second_set)

