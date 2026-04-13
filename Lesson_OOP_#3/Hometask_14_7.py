"""
Сделайте класс Pet абстракным, добавьте метод voice. Подумайте какой метод вам сделать абстрактным,
т.е. что вам удобно будет переопределять.
Проверьте, чтобы подклассы Dog, Cat, Parrot
работали, т.е. вы могли создавать обеъкты.
"""

from abc import ABC, abstractmethod


class Pet(ABC):
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

    @abstractmethod
    def voice(self):
        pass


class Dog(Pet):

    def voice(self):
        print(f"{self.name} лает")


class Cat(Pet):

    def voice(self):
        print(f"{self.name} мяукает")


class Parrot(Pet):

    def voice(self):
        print(f"{self.name} чирикает")


dog = Dog("Бобик", 3, "Иван")
cat = Cat("Барсик", 2, "Петр")
parrot = Parrot("Кеша", 1, "Никита")

dog.run()
dog.jump()
dog.birthday()
dog.sleep()
dog.voice()

cat.run()
cat.jump()
cat.birthday()
cat.sleep()
cat.voice()

parrot.run()
parrot.jump()
parrot.birthday()
parrot.sleep()
parrot.voice()

