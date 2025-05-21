# Collection = single "variable" used to store multiple values
#   List    = [] ordered and changeable. Duplicates OK
#   Set     = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple   = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "banana", "orange", "coconut"]

print(f"Fruits = {fruits}")
print(f"Fruit[0] = {fruits[0]}")
print(f"Fruit[0:2] = {fruits[0:2]}")
print(f"Reversed Fruits = {fruits[::-1]}")
print(f"Length = {len(fruits)}")
print(f"Is apple in fruits?: {"apple" in fruits}")

for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"
fruits.append("apple")
fruits.remove("banana")
fruits.insert(0, "strawberry")
fruits.sort(reverse=True)
fruits.reverse()

print(fruits.index("apple"))
print(fruits.count("pineapple"))

fruits.clear()

print(fruits)
