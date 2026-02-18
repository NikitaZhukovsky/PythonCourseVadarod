"""
Дана строка 'rythm rough rush shake than’. Программа удаляет все буквы «а» в строке и
подсчитывает кол-во удаленных символов
"""

some_str = "rythm rough rush shake than"

print(f"Измененная строка: {some_str.replace('a', '')},"
      f" число удаленных символов 'a': {some_str.count('a')}")

