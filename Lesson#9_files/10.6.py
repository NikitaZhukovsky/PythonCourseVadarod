"""
Прочитать предыдущий файл, сформировать из него множество, распечатать его.
"""

numbers_from_file: set[int] = set()

with open('numbers.txt', 'r') as file:
    for line in file:
        numbers_from_file.add(int(line))

print(numbers_from_file)

