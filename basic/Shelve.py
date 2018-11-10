import shelve

# Auto close after creating
with shelve.open('../data/shelveTest') as fruit:
    fruit['orange'] = 'Sweet, orange and citrus'
    fruit['apple'] = 'Sweet, and good for making cider'
    fruit['lemon'] = 'Sour, yellow, and citrus'
    fruit['grape'] = 'Small, sweet, growing in bunches'
    fruit['lime'] = 'Sour, green, citrus fruit'

# Leave open and manually close
bike = shelve.open('../data/bike')
bike['make'] = 'Honda'
bike['model'] = '250 Dream'
bike['colour'] = 'Red'
bike['engine'] = 250

print(bike['engine'])
bike.close()

print('-' * 50)

# Complex example
blt = ['bacon', 'lettuce', 'tomato', 'bread']
beansOnToast = ['beans', 'bread']
scrambledEggs = ['eggs', 'butter', 'milk']
onionSoup = ['onions', 'bread', 'broth']
pasta = ['noodles', 'sauce', 'parmesan']

with shelve.open('../data/recipes') as recipes:
    recipes['blt'] = blt
    recipes['beans on toast'] = beansOnToast
    recipes['scrambled eggs'] = scrambledEggs
    recipes['pasta'] = pasta

recipes = shelve.open('../data/recipes')
recipes['onion soup'] = onionSoup

tempList = recipes['blt']
tempList.append('mayo')
recipes['blt'] = tempList

for snack in recipes:
    print(snack, recipes[snack])

recipes.close()

print('-' * 50)

with shelve.open('../data/recipes', writeback=True) as recipes:
    recipes['onion soup'].append('salt')
    recipes['onion soup'].append('pepper')

    for snack in recipes:
        print(snack, recipes[snack])
