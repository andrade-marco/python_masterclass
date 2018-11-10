from time import time, perf_counter, monotonic, process_time, get_clock_info

clocks = {'time': time, 'perf_counter': perf_counter, 'monotonic': monotonic, 'process_time': process_time}
for item in clocks:
    time = clocks[item]()
    info = get_clock_info(item)
    print('-' * 100)
    print('Type: {} \t Value: {} \nInfo: {}'.format(item, time, info))
