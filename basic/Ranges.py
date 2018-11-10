# Ranges
###############

# Simple example
newRange = range(10)
newList = list(newRange)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(newList)
print(even)
print(odd)

# Separator
print('*' * 40)

# Ranges are usable with lists
soloRange = range(0, 15000, 3)
print(soloRange[201])
