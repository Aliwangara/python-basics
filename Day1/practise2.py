#Shopping Cart Program

items = input("What do you want to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many items do you want? "))
total = price * quantity

print(f"you chose {items} worth KSH{total}")


