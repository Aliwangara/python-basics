my_file = open('greeting.txt', 'r') # r means read only you cant edit the file being opened
# print(my_file.read())
# print(my_file.read(10)) # Picks 10 characters from the other file. You can specify the number of lines you want.
# print(my_file.readline()) # prints first line of the other file
# print(my_file.readline()) # prints second line of the other file and etc

line_by_line = my_file.readlines() #['Hello,', 'Welcome to Monty Pythons Flying Circus!']
line_by_line1 = my_file.read().splitlines() # ['Hello,', 'Welcome to Monty Pythons Flying Circus!']
# print(line_by_line)
# print(line_by_line1)

my_file.close() # always make sure you close the file after performing operations on it

# To always make sure the file clodses even without calling the close function we use

with open('friends.csv', 'r') as f:
    friends = f.read().splitlines()
    print(friends)

    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} would be {2030- year} Years Old')

# Or the other way we can use:

with open("movies.txt", 'r') as f:
    for line in f:
        print(line)

