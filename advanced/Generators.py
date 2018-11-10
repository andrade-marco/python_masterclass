import sys

def my_range(n):
    start = 0
    while start < n:
        yield start
        start += 1

big_range = range(10000)
new_range = my_range(10000)
print('big_range is {} bytes | new_range is {} bytes'.format(sys.getsizeof(big_range), sys.getsizeof(new_range)))

# Create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print('big_list is {} bytes'.format(sys.getsizeof(big_list)))
