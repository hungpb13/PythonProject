# Sorting: .sort() and sorted()
# List[], Tuple(), Dict{key:value}, Object

print("----- List -----")
fruits = ["banana", "orange", "apple", "pineapple", "coconut"]
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print("----- Tuple -----")
numbers = (69, 8, 56, 32, 74, 62, 98, 28)
print(numbers)

# AttributeError: 'tuple' object has no attribute 'sort'
# numbers.sort()

# sorted(tuple) --> list []
numbers = sorted(numbers)
print(numbers)

numbers = tuple(sorted(numbers, reverse=True))
print(numbers)

print("----- Dict -----")
students = {
    "Bob": 7.5,
    "Daniel": 4.0,
    "Alice": 8.0,
    "Emily": 6.5,
    "Charles": 9.5
}

print(students)

# Return a sorted list of keys
# students = sorted(students)

# Return a sorted list of tuple
# [('Alice', 8.0), ('Bob', 7.5), ('Charles', 9.5), ('Daniel', 4.0), ('Emily', 6.5)]
# students = sorted(students.items())

# Sort by key
students = dict(sorted(students.items()))
print(students)

# Reversed by key
students = dict(sorted(students.items(), key=lambda item: item[0], reverse=True))
print(students)

# Sort by value
students = dict(sorted(students.items(), key=lambda item: item[1]))
print(students)

# Reverse by value
students = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
print(students)

print("----- Object -----")


class Car:
    def __init__(self, model, hp):
        self.model = model
        self.hp = hp

    def __repr__(self):
        return f"{self.model}: {self.hp}(hp)"


cars = [
    Car("Ford Mustang", 560),
    Car("BWM i7", 400),
    Car("Honda Civic", 250),
    Car("Toyota Camry", 200),
    Car("Nissan GTR", 600)
]

print(cars)

# Sort by model
cars = sorted(cars, key=lambda car: car.model)
print(cars)

# Reverse by model
cars = sorted(cars, key=lambda car: car.model, reverse=True)
print(cars)

# Sort by hp
cars = sorted(cars, key=lambda car: car.hp)
print(cars)

# Reverse by hp
cars = sorted(cars, key=lambda car: car.hp, reverse=True)
print(cars)
