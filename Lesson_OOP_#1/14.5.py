"""
Добавьте в класс Porsche метод, который считает
пробег, а также выводит пробег и сколько за сегодня проехал порш.
Создайте 1 порш и 2 раза вызовите метод
"""

class Porsche:
    model = "911"

    def __init__(self, color: str, year: int):
        self.color = color
        self.year = year
        self.mileage = 0.0

    def add_mileage(self, mileage: float):
        self.mileage += mileage
        print(f"Сегодня проехал: {mileage} км")
        print(f"Общий пробег: {self.mileage} км")


first_porsche = Porsche("Red", 2023)
second_porsche = Porsche("Black", 2024)


print(f"Модель порше 1: {first_porsche.model}")
print(f"Цвет порше 1: {first_porsche.color}")
print(f"Год выпуска порше 1: {first_porsche.year}")
print(f"Модель порше 2: {second_porsche.model}")
print(f"Цвет порше 2: {second_porsche.color}")
print(f"Год выпуска порше 2: {second_porsche.year}")

print("Порше 1")
first_porsche.add_mileage(50.5)
first_porsche.add_mileage(30.2)

print("Порше 2")
second_porsche.add_mileage(25.0)
second_porsche.add_mileage(15.8)

