
num = int(input("Enter a number: "))

if num >0:
    print("The number is a positive integer")
    if num % 2 == 0:
        print("The number is an even number")
    else:
        print("The number is an odd number")

elif num <0:
    print("The number is a negative number")
    if num % 2 == 0:
        print("The number is an even number")
    else:
        print("The number is an odd number")
else:
    print("The number is zero")


marks = float(input("Enter your marks to know about your grade: "))

if 90 <= marks <=100:
    print("A")
elif 80 <= marks <=89:
    print("B")
elif 70 <= marks <=79:
    print("C")
elif 60 <= marks <=69:
    print("D")
elif marks < 60:
    print("E")
elif marks < 0 or marks > 100:
    print("Invalid Entry")
else:
    print("F")

