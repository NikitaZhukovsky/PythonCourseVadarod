"""
Прочитать из файла числа, сформировать список и напечатать его
"""

result: list[int] = []

with open('numbers.txt', 'r') as file:
    for line in file:
        result.append(int(line))

print(result)

