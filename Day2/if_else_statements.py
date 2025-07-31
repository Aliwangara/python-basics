#- Do something IF some conditions are true
#     Else do something else
from django.template.defaultfilters import yesno, upper

# age = int(input("Enter your age: "))
#
#
# if age>=100:
#     print("You are Over the Age")
# elif age>=18:
#     print("You are now signed Up")
# elif age<0:
#     print("You arent born Yet")
#
#
# else:
#     print("You are not Eligible")

response = upper(input("Would you like food? (Y/N):"))

if response == 'Y':
    print("Food")
elif response == 'N':
    print("No Food")

menu = input("What would you like to eat? ")

if menu =="":
    print("Please enter a food")
else:
    print(f"You have ordered {menu}")

#Boolean for if statements:

for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

