# three loop questions:
#     1.  What do I want to repeat
#     2.  what do I want to change each time
#     3.  What should I keep repeating

# while condition:
#     code
#     iterator

print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

i = 0
while i < 5:
    i = i+1
    print(f"{i}." + "*"*i + "Loops are awesome" + "*" * i)


# exercise




# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
x = 1
while x<=3:
    x+=1
    question = """Who is The President of kenya
                    A. Uhuru Kenyatta
                    B. Mwai Kibaki
                    C. William Ruto
                    D. Museveni
                    """
    print(question)

    guesses = input("Enter Your guesses(A / B / C/ D):  ").lower()

    if guesses == "a":
        print(f"{guesses} wrong try again")
        continue
    elif guesses == "b":
        print(f"{guesses} wrong try again")
    elif guesses == "c":
        print(f"correct, {guesses} is the president of Kenya ")
        break
    elif guesses == "d":
        print(f"{guesses} wrong try again")
    else:
        print("Please choose a leader from the multiple choices")

    print(" sorry You have exhausted your chances")






y = 0
guess_limit = 8

while y<=guess_limit:
    y+=1
    number = 10

    user_guesses = int(input("Enter a number between 1 and 100:   "))

    if user_guesses == number:
        print(f"===== Congratulations You got the Right number {user_guesses} =====")
        break
    elif user_guesses >=1 and user_guesses<=9:
        print(f"You are close to the number please try again and remember you have {guess_limit-y} chances left ")
    elif user_guesses >=11 and user_guesses <=20:
        print(f"You are close to the number please try again and remember you have {guess_limit - y} chances left ")
    elif user_guesses >=21:
        print(f"You are away from the number please try a smaller number you have {guess_limit - y} chances left ")
    if guess_limit <= y:
     print("Sorry you have exhausted your chances")
     break



























