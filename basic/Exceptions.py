def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    print(factorial(1000))
except RecursionError:
    print('Cannot calculate factorials that large')
except ZeroDivisionError:
    print('Cannot divide by zero')

# Alternative 1
try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError) as error:
    print('An error occured: ' + str(error))

# Alternative 2
try:
    print(factorial(1000))
except Exception as error:
    print('An error occured: ' + str(error))
