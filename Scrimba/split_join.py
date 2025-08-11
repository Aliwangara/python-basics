
msg ='  Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']

print(msg)
# stripped_msg = msg.strip()
#
# print(stripped_msg)


print(msg.split()) # splits the string into a list eg: ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
print(csv.split(',')) # this splits the string into a list after the comma eg:['Eric', 'John', 'Michael', 'Terry', 'Graham']
print('-'.join(friends_list)) # turns a list into a string '-' the character in the middle of the quotation mark is a
                            # separator eg: Eric-John-Michael-Terry-Graham

# greeting  = input('What is your word? ')
#
# reverse =greeting[::-1]
#
# join = ''.join(reverse)
#
# if greeting == join:
#     print("They match in reverse")
# elif  not greeting == join:
#     print("They don't match in reverse")
#
#
#
#
# print(join)

#exercise

csv_2 = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends = []
print(friends)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise


csv2 = ''.join(csv_2).replace(':', ',').replace(';', ',').split(',')
friends = csv2

print(friends)

palindrome = input("Enter Palindrome: ").lower()

palindrome =' '.join(palindrome)[::-1]
answer = palindrome.replace(' ', '')
print(answer)


