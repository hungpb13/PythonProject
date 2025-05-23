# Duck typing = another way to achieve polymorphism beside Inheritance
# Object must have the minimum necessary attributes/methods
# "If it looks like a duck and quack like a duck, then it must be a duck"

class Animal:
    alive = True


class Duck(Animal):
    def speak(self):
        print("QUACK!")


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car:
    alive = False

    def speak(self):
        print("HONK!")


animals = [Duck(), Dog(), Cat(), Car()]

for animal in animals:
    print(f"Alive: {animal.alive}")
    animal.speak()
