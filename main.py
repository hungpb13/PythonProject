# Collection = single "variable" used to store multiple values
#   List    = [] ordered and changeable. Duplicates OK
#   Set     = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple   = () ordered and unchangeable. Duplicates OK. FASTER

fruits = {"apple", "banana", "orange", "coconut", "apple"}

print(f"Fruits = {fruits}")

print(f"Length = {len(fruits)}")
print(f"Is apple in fruits?: {"apple" in fruits}")

for fruit in fruits:
    print(fruit)

fruits.add("pineapple")
fruits.remove("apple")

print(fruits)