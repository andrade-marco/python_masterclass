# While Loops
##########################

# Simple game
chosenExit = ''
availableExits = ['east', 'north east', 'south']

while chosenExit not in availableExits:
    chosenExit = input('Please choose a direction: ')
    if chosenExit == 'quit':
        print('Game over')
        break
else:
    print('You have escaped! Congratulations!')

# Guessing game
import random

highest = 206
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}'.format(highest))
guess = int(input())

while guess != answer:
    if guess > answer:
        print('Too high...')
    else:
        print('Too low...')
    print('Try again: ')
    guess = int(input())
else:
    print('Congratulations! You got it!')
