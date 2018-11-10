def fact(n):
    # Calculate n! iteratively
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def fact_recursive(n):
    # n! can also be defined as n * (n - 1)!
    if n <= 1:
        return 1
    else:
        return n * fact_recursive(n - 1)


def fib(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus_one = 1
        n_minus_two = 0
        for i in range(1, n):
            result = n_minus_two + n_minus_one
            n_minus_two = n_minus_one
            n_minus_one = result
    return result


def fib_recursive(n):
    # Calculate Fibonacci sequence
    if n < 2:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


print('Factorial')
for i in range(30):
    fact_reg = fact(i)
    fact_rec = fact_recursive(i)
    print('{}: {:5} | {:5}'.format(i, fact_reg, fact_rec))

print('-' * 50)

print('Fibonacci')
for i in range(30):
    fib_reg = fib(i)
    fib_rec = fib_recursive(i)
    print('{:2}: {:9} | {:9}'.format(i, fib_reg, fib_rec))
