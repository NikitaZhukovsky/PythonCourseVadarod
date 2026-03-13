"""
Дан список [5, True, ‘abc’].
Записать его в файл
"""

some_list = [5, True, 'abc']

with open('list.txt', 'w') as file:
    file.write(str(some_list))

