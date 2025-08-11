# This exercise combines first 7 python topics: variables, input, strings and slicing, timing, lists, datatype, basic math


# Your task:
# Write a program that simulates a small store checkout system.
#
# Requirements:
# Ask the user for:
#
# Their name (capitalize it).
#
# The name of the item they want to buy.
#
# The price of the item (float).
#
# How many units they want to buy (integer).
#
# Ask the user if they want:
#
# Price in Ksh or USD (if USD, convert using 1 USD = 150 Ksh).
#
# Calculate:
#
# The total cost.
#
# Add a 16% VAT to the cost.
#
# Give a 10% discount if the quantity is greater than 5.
#
# Store the purchased item(s) in a list and display them.
#
# Output:
#
# Name of the buyer.
#
# Item name.
#
# Quantity.
#
# Price per item.
#
# Total cost after VAT & discount.
#
# A thank-you message.

name = input("Enter your name: ").capitalize()
item = input("Which Item Do you wan to buy? ")
price = float(input("Enter The price of the item: "))
quantity = int(input("How many items do you want? "))
currency = input("What currency do you want? (USD or KSH):  ").upper()

purchased_items = []

if currency == "USD":
   price = price * 150

elif currency == "KSH":
  price =  price / 150

total = price * quantity


if quantity > 5:
   quantity_total = total*0.10
   total -= quantity_total

vat = total *0.16
total += vat
purchased_items.append(item)


print("------ INVOICE -------")

print(f"Hello {name} \n Today you purchased {quantity} {item}(s)  which is {price:.2f}/item \n and Total cost is: {total:.2f} {currency}. \n THANK YOU AND MAKE SURE YOU COME AGAIN!")















