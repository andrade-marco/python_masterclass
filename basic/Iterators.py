# Iterators
# Some objects/data structures in Python are iterable

string = 'This is a string'
for char in string:
    iterator = iter(char)
    print(iterator)
    print(next(iterator))

newList = ['a', 'b', 'c', 'd', 'e', 'f']
iterator = iter(newList)

for i in range(len(newList)):
    print(next(iterator))
