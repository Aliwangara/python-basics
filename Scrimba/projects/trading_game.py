import random as r

from Scrimba.exercises.dictionaries_exercise import purse

bag = ('green','green','green','green','green','green','red','red','red','red')

start_purse = 1000

result = 0

rounds = 3

marble = 'none'

print(f'You start the game with {start_purse} gold pieces')

for draw in range(1,rounds+1):

    bet = float(input(f'Current Purse: {start_purse} Last draw: {marble} \nRound {draw} - How much do you want to bet?: '))

    marble = r.choice(bag)

    if marble == 'green':
        result = bet
    else:
        result = -bet

    purse += result

    if purse <0.5 * start_purse:
        print(f'Game over! You lost to much gold!!!')
        break
    print(f'purse: {purse}, last result: ({marble}): {result}')

    print('')

print('starting/ ending purse: ', start_purse, '/',purse)
print('gain/loss: ', ((purse-start_purse)/start_purse *100),'%')

