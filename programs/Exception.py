# Challenge for expections
def division(num, den):
    return int(num) / int(den)

print('------- DIVISION GAME -------')
print()
first_number = input('Please enter the numerator: ')
second_number = input('Please enter the denominator: ')
print()

try:
    result = division(first_number, second_number)
    print('Result is {}'.format(result))
except Exception as e:
    print('Error occured: ' + str(e))
