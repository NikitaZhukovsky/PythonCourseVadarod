"""
Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly, Cat - meow, Dog - bark.
"""

class Dog:
    def __init__(self, name: str, age: int, master: str):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} бегает")

    def jump(self):
        print(f"{self.name} прыгает")

    def birthday(self):
        self.age += 1
        print(f"Возраст {self.name}: {self.age} лет")

    def sleep(self):
        print(f"{self.name} спит")

    def bark(self):
        print(f"{self.name} лает: Гав-гав!")


class Cat:
    def __init__(self, name: str, age: int, master: str):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} бегает")

    def jump(self):
        print(f"{self.name} прыгает")

    def birthday(self):
        self.age += 1
        print(f"Возраст {self.name}: {self.age} лет")

    def sleep(self):
        print(f"{self.name} спит")

    def meow(self):
        print(f"{self.name} мяукает: Мяу-мяу!")


class Parrot:
    def __init__(self, name: str, age: int, master: str):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} бегает")

    def jump(self):
        print(f"{self.name} прыгает")

    def birthday(self):
        self.age += 1
        print(f"Возраст {self.name}: {self.age} лет")

    def sleep(self):
        print(f"{self.name} спит")

    def fly(self):
        print(f"{self.name} летает")


dog = Dog("Бобик", 3, "Иван")
cat = Cat("Барсик", 2, "Петр")
parrot = Parrot("Кеша", 1, "Никита")

dog.run()
dog.jump()
dog.bark()
dog.birthday()
dog.sleep()

cat.run()
cat.jump()
cat.meow()
cat.birthday()
cat.sleep()

parrot.run()
parrot.jump()
parrot.fly()
parrot.birthday()
parrot.sleep()

