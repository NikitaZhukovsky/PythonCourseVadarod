"""
Пользователь вводит слова.
Записать их в файл: каждое слово на отдельной строке
"""

with open('words.txt', 'w') as file:
    print("Введите строки для записи в файл (пустая строка - окончание ввода):")

    while True:
        line = input()
        if line == "":
            break
        file.write(line + '\n')

