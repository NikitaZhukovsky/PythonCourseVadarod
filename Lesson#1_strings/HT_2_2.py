"""
Дана строка 'rythm (rough rush shake) than’. Программа выводит только ту часть строки,
которая НЕ в скобочках.
"""

some_str = "rythm (rough rush shake) than"

print(f"Измененная строка: {some_str[:some_str.find('(')] + some_str[some_str.find(')') + 1:]}")

