# Exercise: Concession Stand Program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

print("----------- MENU ----------")
for key, value in menu.items():
    print(f"{key:20} ${value:.2f}")
print("---------------------------")

while True:
    food = input("Select and item (press Q to quit): ").lower()
    if food.upper() == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------- ORDER ----------")
for food in cart:
    value = menu.get(food)
    total += value
    print(f"{food:22} ${value:.2f}")
print("----------------------------")
print(f"{"Total":22} ${total:.2f}")