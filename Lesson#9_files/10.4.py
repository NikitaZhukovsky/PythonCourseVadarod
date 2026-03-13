"""
Прочитать предыдущий файл, сформировать из него словарь, распечатать его
"""

days: dict[int, str] = {}

with open('days.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        key, value = line.split(':')
        key = int(key)
        days[key] = value

print(days)

