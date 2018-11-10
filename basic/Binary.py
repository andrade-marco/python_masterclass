
# Binary and Hexadecimal
###########################

# Printing binary and hex
for i in range(256 ):
    print('in decimal {0:>08} |  in binary {0:>08b} | in hex {0:>08x}'.format(i))


# Converting decimal to binary
number = int(input('Please enter a number: '))
binary = ''

for i in range(17):
    if number // 2 ** i > 1:
        continue
    else:
        binary = '1'
        remainder = number % 2 ** i
        while (remainder > 0):
            if remainder // 2 ** (i - 1) < 1:
                binary += '0'
            else:
                binary += '1'
                remainder %= 2 ** (i - 1)
            i -= 1
        else:
            binary += '0' * i
        break

print(int(binary))
