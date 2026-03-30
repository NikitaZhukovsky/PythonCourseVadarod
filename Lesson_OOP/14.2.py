"""
Создайте класс Porsche с одним статическим атрибутом (модель) и
несколькими динамическими. Создайте 2 порша
"""


class Porsche:
    model = "911"

    def __init__(self, color: str, year: int):
        self.color = color
        self.year = year


first_porsche = Porsche("Red", 2023)
second_porsche = Porsche("Black", 2024)


print(f"Модель порше 1: {first_porsche.model}")
print(f"Цвет порше 1: {first_porsche.color}")
print(f"Год выпуска порше 1: {first_porsche.year}")
print(f"Модель порше 2: {second_porsche.model}")
print(f"Цвет порше 2: {second_porsche.color}")
print(f"Год выпуска порше 2: {second_porsche.year}")

