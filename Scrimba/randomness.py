
import random,string

print(dir(random))

print(random.random())

for i in range(5):
    # print(random.random()*6)
    #
    print(random.randint(1,6))
    # chooses a number between 1 and 6 we can use  1,6,3 = 1 to 6 and in steps of 3
    print(random.randrange(1,10,2))

print('Randomness')


friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']

print(random.choice(friends_list))
# print(random.sample(friends_list,3))
print(random.shuffle(friends_list))

smallcaps = 'abcdefghijklmnopqrstuvwxyz'

largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits

word = ''
for i in range(7):
    word += random.choice(letters_numbers)
print(word)

word_1 = ''.join(random.sample(letters_numbers, 7))
word = random.choices(letters_numbers, k=7)
print(word)
print(word_1)

print(letters_numbers)

