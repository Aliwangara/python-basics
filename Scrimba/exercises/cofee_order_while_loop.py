# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price

total_price = 0
drink_count = 0

while True:
    name = input("Please Enter your name?if done please write(D):  ").upper()




    if name == "D":
        break
    order = input("What is your order?: ").lower()
    if order == "latte":
        drink_count += 1
        total_price += 3.50
    elif order == "americano":
        drink_count += 1
        total_price += 3.00
    elif order =="espresso":
        drink_count += 1
        total_price += 2.50
    else:
        print("What you want is not in the menu")
        continue


    print(f"======= Hello {name} ======")
    print(f"You bought {drink_count} drinks costing {total_price}")
    print("==== Thank you please Come back again ====")


