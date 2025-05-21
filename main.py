# 2D list =  a list where each element is another list

fruits = ["apple", "banana", "coconut"]
vegetables = ["celery", "potatoes", "carrots"]
meats = ["beef", "chicken", "pork"]

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[0])
print(groceries[0][1])

for foods in groceries:
    for food in foods:
        print(food, end=" ")
    print()