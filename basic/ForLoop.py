# FOR LOOP
#####################

# Simple example 1
number = '9,223,372,786,472,497,234'
cleanNum = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanNum += number[i]

newNumber = int(cleanNum)
print('The number is {}'.format(newNumber))

# Simple example 2
for char in number:
    if char in '0123456789':
        cleanNum += char

newNumber = int(cleanNum)
print('The number is {}'.format(newNumber))

# Range with step
for i in range(0, 100, 5):
    print('{} is the next multiple of 5'.format(i))

# Continue, Break and Else
shoppingList = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
for item in shoppingList:
    if item == 'spam':
        continue  # Skip if item is equal to 'spam'
    print('Buy ' + item)

for item in shoppingList:
    if item == 'spam':
        break
    print('Buy ' + item)

for item in shoppingList:
    if item == 'spam':
        print('No, thank you...')
        break
else:  # Won't be called if 'spam' is in list
    print('Yes, thank you...')
    
