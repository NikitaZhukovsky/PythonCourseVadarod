"""
Создать родительский класс Pet,
содержащий все общие методы классов
Dog, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet.
Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""

class Pet:
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

class Dog(Pet):
    def bark(self):
        print(f"{self.name} лает")


class Cat(Pet):
    def meow(self):
        print(f"{self.name} мяукает")


class Parrot(Pet):
    def fly(self):
        print(f"{self.name} летает")


dog = Dog("Бобик", 3, "Иван")
cat = Cat("Барсик", 2, "Петр")
parrot = Parrot("Кеша", 1, "Никита")

dog.run()
dog.jump()
dog.birthday()
dog.sleep()
dog.bark()

cat.run()
cat.jump()
cat.birthday()
cat.sleep()
cat.meow()

parrot.run()
parrot.jump()
parrot.birthday()
parrot.sleep()
parrot.fly()

