
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
expression = input("Enter expression(* + - / % **): ")

if expression == "+":
   result =  number1 + number2
elif expression == "-":
    result = number1 - number2
elif expression == "*":
    result = number1 * number2
elif expression == "/":
    result = number1 / number2
elif expression == "%":
    result = number1 % number2
elif expression == "**":
    result = number1 ** number2

print(result)
