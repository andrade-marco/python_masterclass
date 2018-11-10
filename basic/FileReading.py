print('************ FILE READING ************')
jabber = open('../data/sample.txt', 'r')
for line in jabber:
    if 'jabberwock' in line.lower():
        print(line, end='')

jabber.close()

# Alternative: with as
with open('../data/sample.txt', 'r') as newJabber:
    for line in newJabber:
        if 'JAB' in line.upper():
            print(line, end='')

print('*' * 40)

# Reading file - readline
with open('../data/sample.txt', 'r') as newJabber:
    line = newJabber.readline()
    while line:
        print(line, end='')
        line = newJabber.readline()

print('*' * 40)

# Reading file - readlines
with open('../data/sample.txt', 'r') as newJabber:
    lines = newJabber.readlines()
for line in lines:
    print(line, end='')

print('*' * 40)

# Reading file - read
with open('../data/sample.txt', 'r') as newJabber:
    lines = newJabber.read()
for line in lines:
    print(line, end='')
