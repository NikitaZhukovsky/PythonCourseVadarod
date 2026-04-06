"""
Добавить классу Dog приватный атрибут - master.
Создать метод get_master() который возвращает значение атрибута master.
"""

class Dog:
    def __init__(self, height: float, weight: float, name: str, age: int):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = None

    def set_master(self, master: str):
        self.__master = master

    def get_master(self):
        return self.__master

    def jump(self):
        print(f"{self.name} прыгает")

    def run(self):
        print(f"{self.name} бегает")

    def bark(self):
        print(f"{self.name} лает")


dog = Dog(0.5, 10.5, "Бобик", 3)

dog.set_master("Хозяин")

print(f"Имя: {dog.name}")
print(f"Возраст: {dog.age} лет")
print(f"Рост: {dog.height} м")
print(f"Вес: {dog.weight} кг")
print(f"Хозяин: {dog.get_master()}")

dog.jump()
dog.run()
dog.bark()

