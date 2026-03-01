"""
Вход: целое число. Вывести для него таблицу умножения от 1 до 10.
Каждая строка таблицы должна показывать результат умножения введённого числа на текущий множитель.
В конце вывести сумму всех полученных результатов.
"""

number = int(input("Введите число: "))

sum_of_results = 0

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} * {multiplier} = {result}")
    sum_of_results += result

print(f"Сумма всех результатов: {sum_of_results}")

