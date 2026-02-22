"""
Программа принимает на вход три строки (потенциальные пароли пользователя) и анализирует их на безопасность по следующим критериям:

Общие символы — вывести символы, которые встречаются во всех трёх паролях (пересечение)

Уникальные символы — вывести символы, которые встречаются только в одном из паролей
Рекомендация — если в пароле меньше 4 уникальных символов, вывести предупреждение "Слабый пароль"
"""


first_password = set(input("Введите первый пароль: "))
second_password = set(input("Введите второй пароль: "))
third_password = set(input("Введите третий пароль: "))


print(f"Символы во всех паролях: {first_password & second_password & third_password}")

print(f"Уникальные символы: {(first_password - second_password - third_password) |
                             (second_password - first_password - third_password) | 
                             (third_password - first_password - second_password)}")

for i, p in enumerate([first_password, second_password, third_password], 1):
    status = "Слабый пароль" if len(p) < 4 else "Надежный пароль"
    print(f"Пароль {i}: {status}")

