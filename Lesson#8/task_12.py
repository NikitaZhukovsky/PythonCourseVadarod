"""
Список из 7 цифр.
Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
если нечетных больше, то найти произведение 1 3 и 6 элемента.
"""

numbers_list = [2, 5, 8, 3, 6, 1, 4]

even_count = 0
odd_count = 0

for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    result = sum(numbers_list)
    print(f"Четных больше ({even_count} > {odd_count}). Сумма всех цифр: {result}")
elif odd_count > even_count:
    result = numbers_list[0] * numbers_list[2] * numbers_list[5]
    print(f"Нечетных больше ({odd_count} > {even_count}). Произведение 1, 3 и 6 элемента: {result}")
else:
    print(f"Четных и нечетных поровну ({even_count} = {odd_count})")

