#Prompt the user to enter data returns data as a string

name = input("What is your name: ")
age = input("How old are you? ")
print(f'You  are: {age}')

# WE Cant increase or perform any arithmetic operation with input unless we converts it so eg:
# age+=1 we get an error so we will need to do int(input("what is your age: " ))'
#This code converts the string fist to an integer and then adds it

age = int(input("How old are you? "))
age+=1

print(f"Hello {name} You are {age}")