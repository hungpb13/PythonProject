# Inheritance = allows a class (child) inherit attributes and methods from another class (parent)
# Help with code reusability and extendability
# class Child(Parent):

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is asleep...")


# Child Class
class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


# Create Objects
dog = Dog("Scoopy")
cat = Cat("Garfield")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
