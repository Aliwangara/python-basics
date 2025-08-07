import random

# print(help(random))
# print(dir(random))
low = 1
high = 100
options  = ('rock', 'paper', "scissors")
number = random.randint(low,high)

cards = ["a", "B", "c", "d", "e", "f", "g", "h", "I", "J", "K"]

option = random.choice(options)

card = random.choice(cards)



print(card)