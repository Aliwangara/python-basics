#python weight calc
from django.template.defaultfilters import upper

weight = float(input("Enter your weight : "))
unit = upper(input("Kilograms or Pounds (K/L): "))

if unit == "K":
    weight = round(weight * 2.205, 1)
    unit = "lbs"
elif unit == "L":
    weight = round(weight / 2.205, 1)
    unit = "kg"
else:
    print(f"{unit} is not a valid unit")

print(f"Your weight is {weight} {unit}")