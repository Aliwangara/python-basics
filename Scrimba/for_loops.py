
# for letter in 'Norwegian blue':
#     print(letter)
#
# print("For Loop done!")

#  a for loop consists of three things in range(start from, End at and steps) eg:

#                   start  stop    steps eg: 1,3,5,7
# for number in range(1     ,20    ,2):
#     print(number)# getting this number 1,3,5,7,9,11,13,15,17,19

# The number ends a digit before the ;ast number eg: if you want the number to end at 20 then we use 21 as stop.

# We can print a list:

# friends = ['John','Terry','Eric','Michael','George']
#
# for friend in friends:
#     print(friend)


# to get a single item in the list we use:
# for index in range(len(friends)):
#     print(friends[index])

# for friend in friends:
#     if friend == "Eric":
#         print(f"found {friend}!")
#         break
#     print(friend)
# print('Done')



# Nested Loop - basically a loop inside a loop

my_friends = [ "Ava", "Liam", "Sophia", "Noah", "Isabella", "Ethan"]

# for friend in my_friends:
    # for number in [1,2,3,4,5]:
        # print(friend, number)

# a nested for loop prints: Sophia 1 # Sophia 2# Sophia 3  Sophia 4 Sophia 5
# same to the other names



# for loops exercise:

names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

combined_names = ','.join(names + names1).lower().title().split(',')


# while True:
#
#     name_input = input("Enter a name write(d) when done: ").title()
#
#
#     if name_input == "D":
#         print(combined_names)
#         break
#     else:
#         combined_names.append(name_input)
#         print(combined_names)
# for name in combined_names:
#     for index in range(len(combined_names)):
#         if name == combined_names[index]:
#             print(f"{name}! You are Invited to the party on Saturday.")


#  or rather we can use:

for index in range(2):
    name_input = input("Enter a name write(d) when done: ").title()

    combined_names.append(name_input)

for name in combined_names:
    print(f"{name}! You are Invited to the party on Saturday.")











