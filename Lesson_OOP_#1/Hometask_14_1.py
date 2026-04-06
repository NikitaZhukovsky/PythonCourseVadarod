"""
Создать класс Dog.
Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark. Каждый
метод выводит сообщение на экран. Создать объект класса Dog, вызвать все
методы объекта и вывести на экран все его атрибуты.
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


dog = Dog(0.5, 10.5, "Бобик", 3)

print(f"Имя: {dog.name}")
print(f"Возраст: {dog.age} лет")
print(f"Рост: {dog.height} м")
print(f"Вес: {dog.weight} кг")

dog.jump()
dog.run()
dog.bark()

