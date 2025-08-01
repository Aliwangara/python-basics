#validate user input
#1. username is no more than 12 characters
#2. username must not contain spaces
#3.username must not contain digits

username = input("Enter your username: ")

length = len(username)
all_alphabets = username.isalpha()

if length >=12:
    print("Your username shouldn't be more than 11 characters")
else:
    print("Correct")

if not all_alphabets:
    print("Your username shouldn't contain any numeral or special characters")
else:
    print("Correct")

if username.find(" "):
    username = username.replace(" ", "")
    print(username)

else:
    print("Correct no spaces")