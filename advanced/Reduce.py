import functools
import timeit

def calc_values(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5, 6]

reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
