# Class variable = shared among all instances of a class
# Defined outside the constructor __init__(self)

class Student:
    # Class variable
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


alice = Student("Alice", 20)
bob = Student("Bob", 30)

print(f"Class year: {Student.class_year}")

print(alice.name)
print(alice.age)
print(alice.class_year)

print(bob.name)
print(bob.age)
print(bob.class_year)

print(f"Num of students: {Student.num_students}")

charles = Student("Charles", 25)
daniel = Student("Daniel", 35)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
