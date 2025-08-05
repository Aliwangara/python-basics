
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit)")
    if food.lower() == "q":
     break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of a {food}: $ "))
        prices.append(price)

print("---Your Cart----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"Total: ${total:10.2f}")