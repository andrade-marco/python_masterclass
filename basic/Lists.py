# Lists
###################
activities = ['hiking', 'surf', 'soccer', 'tennis']
activities.append('biking')
newActivities = sorted(activities)

for item in activities:
    print('The next activity is {}'.format(item))

for item in newActivities:
    print('The next sorted activity is {0}'.format(item))

# List constructor
listOne = list()
listTwo = list('This will be split')

# in operator
menu = []
menu.append(['eggs', 'spam', 'bacon'])
menu.append(['eggs', 'bacon', 'sausage'])
menu.append(['eggs', 'bacon', 'sausage', 'spam'])

for meal in menu:
    if 'spam' not in meal:
        for item in meal:
            print(item)
