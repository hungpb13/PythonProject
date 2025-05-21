# Exercise: Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press Q to quit): ")
    if food.upper() == "Q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("---- YOUR CART ----")

for i in range(len(foods)):
    print(f"{foods[i]}\t\t\t${prices[i]}")

print("-------------------")

for price in prices:
    total += price
print(f"Your total is: ${total:.2f}")
