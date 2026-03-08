"""
Программа принимает список из трех слов. Создать словарь, в котором ключ — слово,
значение — количество символов в слове
"""

words_list = input("Введите 3 слова через пробел: ").split()

word_lengths = {word: len(word) for word in words_list}

print(word_lengths)

