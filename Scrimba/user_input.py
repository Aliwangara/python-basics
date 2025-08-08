#
# name = input("Enter your name: ").capitalize()
# age = input("Enter your age: ")
#
# print(f"hello {name}! you are {age} years old.")
#
# number_1 = float(input("Enter your first number: "))
# number_2 = float(input("Enter your second number: "))
#
# total  =number_1 + number_2
#
# print(f"Your total is {total}")

#exercise
first_name = input("Enter your first name: ").capitalize()

distance = float(input("Enter your distance: "))
values = input("Km or Mi: ").capitalize()

if values == "Km":
    distance  = (distance * 1)/ 1.609
    print(f"{first_name} Your distance is {distance:.2f} miles")
elif values == "Mi":
    distance  = distance *1.609
    print(f"{first_name} Your distance is {distance:.2f} kilometers")
else:
    print("Invalid input")





