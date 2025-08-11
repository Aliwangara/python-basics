# 1. You are managing a small store for your friends.
# Some friends are already in your database, but the list is messy and stored in multiple formats (string, list, set).
# Your task is to clean the data, find mutual friends, handle purchases, and generate an invoice.

messy_friends = "Ali,John;Wangara:Eric,,Michael:Anna"
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

messy_friends = ''.join(messy_friends).replace(':', ',').replace(';', ',').replace(',,', ',')
friends_list = messy_friends.split(',')
friends_list = set(friends_list)

friends_set = friends_set.union(friends_list)

print(friends_set)

# step 2:
#Find friends that are in both your set and my_friends_set.
# Find friends that are only in your set.
# Find friends that are only in my_friends_set.
# Find friends that appear in only one of the sets (symmetric difference).

# friends_set = friends_set.intersection(my_friends_set)


my_set = friends_set.difference(my_friends_set)
print(my_set)

my_friends_set = my_friends_set.difference(friends_set)

print(my_friends_set)

sy_difference = friends_set.symmetric_difference(my_friends_set)
print(sy_difference)

# #step3.
# Ask the user:
# Name (capitalize)
# Item they want to buy
# Price per item (float)
# Quantity (integer)
# Currency (KSH or USD) — if USD, convert to KSH (1 USD = 150 KSH)
# If quantity > 5 → give 10% discount.
# Add 16% VAT to final amount.

name  = input('Enter your name: ').capitalize()
item = input('Enter an item you want to buy: ').capitalize()
price = float(input('Enter the price per item: '))
quantity = int(input('Enter the number of items: '))
currency = input("Enter the currency you are using (USD or KSH): ").capitalize()

if quantity > 5:
   price =  price * 0.10

vat = price * 0.16

final_price = price * quantity + vat


# step 4:
#Print an invoice showing:
# Buyer’s name
# Mutual friends (from Step 2)
# Purchased item
# Price per item (after currency conversion)
# Quantity
# Final cost (after VAT & discount)
# A thank-you message

print("---- INVOICE ----")

print(f"Hello {name} Your mutual friends are {sy_difference}\n - you purchased {item}(s)\n price per item is {price} and you bought {quantity}\n"
      f"this brings your final cost after (VAT and Discount to {final_price} {currency} ")


