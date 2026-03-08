"""
Даны 2 списка:
a = [4,6,'pу','tell',78]
b = [44,'hello’,56,'exept’,3]
Выполнить следующие операции:
1) Сложить два списка
2) Добавьте элемент 6 на 3 позицию.
3) Удалите все текстовые переменные
4) Посчитайте количество элементов списка
"""

a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]

sum_of_lists = a + b
print(f"1) {sum_of_lists}")

sum_of_lists.insert(2, 6)
print(f"2) {sum_of_lists}")

numbers_list = [number for number in sum_of_lists if isinstance(number, int)]
print(f"3) {numbers_list}")

count_elements = len(numbers_list)
print(f"4) {count_elements}")

