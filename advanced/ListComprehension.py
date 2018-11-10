# Generating squares
numbers = [1, 2, 3, 4, 5, 6]
squares = []
squares_comp = [number ** 2 for number in numbers]

for number in numbers:
    squares.append(number ** 2)

print(squares)
print(squares_comp)

print('-' * 40)

text = 'what have the romans ever done for us'
capitals = [char.upper() for char in text]
print(capitals)

print('-' * 40)

def centre_text(*args):
    text = '-'.join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text)

centre_text('spam and eggs')
centre_text('spam, spam, and eggs')
centre_text(12)
centre_text('spam, spam, spam, and spam')
centre_text(1, 2, 3, 'are all words')

print('-' * 40)

menu = [
    ['egg', 'spam', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['egg', 'chicken', 'chips']
]

meals = []
for meal in menu:
    if 'spam' not in meal:
        meals.append(meal)
    else:
        meals.append('Meal skipped')

print(meals)

# Simple
meals = [meal for meal in menu if 'spam' not in meal]
print(meals)

# With conditional expression
meals = [meal if 'spam' not in meal else 'Meal skipped' for meal in menu]
print(meals)
