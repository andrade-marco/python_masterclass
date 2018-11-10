# Sets
###############

farmAnimals = {'sheep', 'cow', 'hen'}
farmAnimals.add('horse')
print(farmAnimals)

for animal in farmAnimals:
    print(animal)

print('*' * 40)

wildAnimals = set(['lion', 'tiger', 'panther'])
wildAnimals.add('cheetah')
print(wildAnimals)

for animal in wildAnimals:
    print(animal)

print('*' * 40)

# Create sets out of any iterable object
even = set(range(0, 40, 2))
squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)

evenUnion = even.union(squares)
evenIntersection = even.intersection(squares)
evenMinus = even.difference(squares)

print(evenUnion)
print(evenIntersection)
print(even & squares)
print(evenMinus)
print(even - squares)
