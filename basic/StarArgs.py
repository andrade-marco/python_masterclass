#Star args and double-star Kwargs

def average(*args):
    print(type(args))
    print('args is {}'.format(args))
    print('*args is ', *args)
    mean = 0
    for arg in args:
        mean += arg

    return mean / len(args)


def build_tuple(*args):
    return args


def max_number(*args):
    max = args[0]
    for num in args:
        if num > max:
            max = num

    return max


def min_number(*args):
    min = args[0]
    for num in args:
        if num < min:
            min = num

    return min


def print_backwards(*args, **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], **kwargs)


print(average(1,2,4,6,8))
print(max_number(1,2,3,4,5,6,7))
print(min_number(5,7,9,3,4))
just_tuple = build_tuple('a','b','c','d','e','f')
print(type(just_tuple))
print(just_tuple)

with open('backwards.txt', 'w') as backwards:
    print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end=' ', file=backwards)

print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end=' ')
