import time

print('time():              ',time.get_clock_info('time'))
print('perf_counter():      ',time.get_clock_info('perf_counter'))
print('monotonic():         ',time.get_clock_info('monotonic'))
print('process_time():      ',time.get_clock_info('process_time'))