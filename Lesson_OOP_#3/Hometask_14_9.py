"""
Добавьте в класс Pet валидацию, чтобы у питомца было имя и хозяин.
"""

from abc import ABC, abstractmethod


class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'Возраст должен быть > 0')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class NonEmptyMasterAndName:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value.strip():
            raise ValueError(f'{self.name} не может быть пустым')
        instance.__dict__[self.name] = value.strip()

    def __set_name__(self, owner, name):
        self.name = name


class Pet(ABC):

    age = NonNegative()
    name = NonEmptyMasterAndName()
    master = NonEmptyMasterAndName()

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


dog = Dog("Бобик", 3, "")
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

