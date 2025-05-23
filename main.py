# Multiple inheritance = a child class inherits from more than one parent class
# class C(A, B):
# Multilevel inheritance = a child class inherits from a parent which inherits from a grandparent class
# class C(B): <-- class B(A): <-- class A:

# Method Resolution Order (MRO) is the order in which Python looks for a method or attribute 
# when multiple classes are involved — especially in multiple inheritance.
# Python uses the C3 linearization algorithm to determine the MRO.

# Grandparent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")

    def speak(self):
        print(f"{self.name} is speaking...")


# Parent Class
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting...")

    def speak(self):
        print(f"{self.name} is mmmm...")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing...")

    def speak(self):
        print(f"{self.name} is zzzz...")


# Child Class
class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


# Multiple inheritance
# Method Resolution Order (MRO) = Fish < Prey < Predator < Animal
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
fish.speak()
print(Fish.mro())
