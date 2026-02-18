"""
Дана строка 'rythm rough rush shake than’. Программа выводит строку, в которой
последовательность символов между первым и последним появлением буквы ‘h’
повернута в противоположном порядке
"""

some_str = "rythm rough rush shake than"

first_part, last_part = some_str.find('h'), some_str.rfind('h')

result = some_str[:first_part+1] + some_str[first_part+1:last_part][::-1] + some_str[last_part:]

print(f"Измененная строка: {result}")

