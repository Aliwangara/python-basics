#conditionals IF statements

print("conditional if else statements")

is_raining = True
is_cold = False

print("Good morning")

if is_raining and is_cold:
    print("bring umbrella and jacket")
elif not is_raining and is_cold:
    print("bring Jacket")
elif is_raining and not is_cold:
    print("Bring Umbrella")
else:
    print("Weather is fine")



#exercise

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
calc_operator = input("Operator ( + - * /): ")

if calc_operator == "+":
    result = first_number + second_number
    print(result)
elif calc_operator == "-":
    result = first_number - second_number
    print(result)
elif calc_operator == "*":
    result = first_number * second_number
    print(result)
elif calc_operator == "/":
    result = first_number / second_number
    print(result)
else:
    print("invalid operator")

temperature = float(input("Enter temperature: "))
unit =input("Enter unit (C or F): ").upper()

if unit == "C":
    temperature = temperature * 9/5 + 32
    print(f"Temperature is {temperature} fahrenheit")






