#while_loop = execute some condition while some condition remains true

# name   = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     input("Enter your name: ")
# print(f"Hello {name}")
#
# age =  int(input("Enter your age: "))
#
# while age<0 :
#     print("age cant be negative")
#     age = int(input("Enter your age: "))
# print(f"Your age is {age}")

# food = input("Enter your favorite food (q to quit): ")
#
# while not food == "q":
#     print(f"your favorite food {food}")
#     food = input("Enter your favorite food (q to quit): ")
# print(f"Bye")

num = float(input("Enter a number between 1 and 10 (-1 to quit): "))

while num < 1 or num > 10 :
    print(f"{num} Invalid number")
    num = float(input("Enter a number between 1 and 10: "))
print(f"Your number is {num}")


number  = float(input("Enter a number between 1 and 20: "))

while number <10  or number >20:
    print(f"{number} Invalid number")
    number = float(input("Enter a number between 1 and 20: "))
print(f"Your number is {number}")

if number >10 or number <20:
    print(f"Your number is {number}")
else:
  num = float(input("enter your number"))
