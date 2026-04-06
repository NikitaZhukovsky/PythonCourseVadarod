"""
Добавить в класс Dog метод change_name.
Метод принимает на вход новое имя и меняет атрибут имени у
объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя
"""


class Dog:
    def __init__(self, height: float, weight: float, name: str, age: int):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"{self.name} прыгает")

    def run(self):
        print(f"{self.name} бегает")

    def bark(self):
        print(f"{self.name} лает")

    def change_name(self, new_name: str):
        self.name = new_name

dog = Dog(0.5, 10.5, "Бобик", 3)

print(f"Имя: {dog.name}")

dog.change_name("Шарик")

print(f"Измененное имя: {dog.name}")

print(f"Возраст: {dog.age} лет")
print(f"Рост: {dog.height} м")
print(f"Вес: {dog.weight} кг")

dog.jump()
dog.run()
dog.bark()

