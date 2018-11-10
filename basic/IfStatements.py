# IF STATEMENTS
#####################

# Simple statements 1
name = input('Please enter your name: ')
age = int(input('How old are you, {0}?'.format(name)))
print(age)

if age >= 18:
    print('You are old enough to vote')
else:
    print('Please come back in {0}'.format(18 - age))

# Simple statements 2
print('Please guess a number between 1 and 10: ')
guess = int(input())

if guess != 5:
    if guess < 5:
        print('Please guess higher')
    else:
        print('Please guess lower')

    guess = int(input())
    if guess == 5:
        print('Well done, you guessed it')
    else:
        print('Sorry, you have not guessed correctly')
else:
    print('You got it first time')

# More advanced statements
newAge = int(input('How old are you?'))

if (newAge >= 16) and (newAge <= 65):
    print('Have a good day at work')

if 16 <= newAge <= 65:  # 15 < newAge < 66
    print('Have a good day at work')

if (newAge < 15) or (newAge > 65):
    print('Enjoy your free time')
else:
    print('Have a good day at work')
