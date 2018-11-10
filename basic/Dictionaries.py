# Dictionaries
########################
item = 'lemon'
fruit = {'lemon': 'Sour and yellow, good in drinks.',
         'orange': 'Sweet and orange, perfect in old fashioned cocktails.',
         'grape': 'Sweet and dark purple, used to make wine.',
         'apple': 'Sweet and crunchy, keeps the doctors away.'}

keyList = list(fruit.keys())
valueList = list(fruit.values())
itemTuple = tuple(fruit.items())
fruitDic = dict(itemTuple)
print('Getting dictionary keys/values/items')
print(keyList)
print('-' * 40)
print(valueList)
print('-' * 40)
print(itemTuple)
print('-' * 40)

for key in sorted(fruit):
    print(key + ' - ' + fruit[key])

while True:
    dictKey = input('Please enter a fruit name: ')
    if dictKey == 'quit':
        break
    elif dictKey == '':
        continue
    message = fruit.get(dictKey, dictKey + ' is not available...')
    print(message)
