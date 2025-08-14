
# in this enumerate is a python function that allows one instead of using an iterator to use build in function to count a
# loop eg:

# Old method:

print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

# i = 0 - the iterator starts from0 but if you want it to start from 1 you can use:
i= 1

for friend in friends:
    print(i, friend)
    i+=1

#  NEW WAY TO DO THIS IS:
#                                     this 1 is the same as i=1 or i=0 meaning start counting from 1
for num, friend in enumerate(friends, 51):
    print(num ,friend)

# What num does:

# efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]
#     - Num converts elements inside the list individually into a tuple as shown above.