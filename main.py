# Multiple inheritance = a child class inherits from more than one parent class
# class C(A, B):
# Multilevel inheritance = a child class inherits from a parent which inherits from a grandparent class
# class C(B): <-- class B(A): <-- class A:

# Grandparent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")


# Parent Class
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing...")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting...")


# Child Class
class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


# Multiple inheritance
class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
rabbit.eat()
rabbit.sleep()

hawk.hunt()
hawk.eat()
hawk.sleep()

fish.flee()
fish.hunt()
fish.eat()
fish.sleep()
