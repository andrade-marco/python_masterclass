import timeit
from statistics import mean, stdev

setup = """\
gc.enable()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

def nested_loop():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
    return result

def loop_comp():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
    return result

def nested_comp():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations)]
    return exits_to_destination_3

timing = [[],[],[]]
for i in range(100):
    timing[0].append(timeit.timeit(nested_loop, setup, number=1000))
    timing[1].append(timeit.timeit(loop_comp, setup, number=1000))
    timing[2].append(timeit.timeit(nested_comp, setup, number=1000))

print('Nested loop (min): \t{}'.format(min(timing[0])))
print('Loop comp (min): \t{}'.format(min(timing[1])))
print('Nested comp (min): \t{}'.format(min(timing[2])))

print('-' * 50)

# Using functions with arguments with timeit
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    print(timeit.timeit('x = fact(130)', setup='from __main__ import fact', number=1000))
    print(timeit.timeit('x = factorial(130)', setup='from __main__ import factorial', number=1000))

    print('--Repeating test--')
    fact_list = timeit.repeat('x = fact(130)', setup='from __main__ import fact', number=1000, repeat=6)
    factorial_list = timeit.repeat('x = factorial(130)', setup='from __main__ import factorial', number=1000, repeat=6)
    print(min(fact_list), mean(fact_list), stdev(fact_list))
    print(min(factorial_list), mean(factorial_list), stdev(factorial_list))
