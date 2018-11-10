import time
import datetime
import pytz
import random
from time import time as my_timer

# input('Press enter to start')
#
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
#
# input('Press enter to stop')
# end_time = my_timer()
#
# print('Started at ' + time.strftime('%X', time.localtime(start_time)))
# print('Ended at ' + time.strftime('%X', time.localtime(end_time)))
#
# print('Your reaction time was {} seconds'.format(end_time - start_time))

# Getting basic time information
print('----- USING TIME MODULE ------')
print('Epoch starts at ' + time.strftime('%c', time.gmtime(0)))
print('Current timezone: {0} with an offset of {1}.'.format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print('Daylight Saving Time in effect')
    print('The DST timezone is ' + time.tzname[1])

print('Local time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print('UTC time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
print('-' * 100)
print()

print('----- USING DATETIME MODULE ------')
print('Local time (using today()): {}'.format(datetime.datetime.today()))
print('Local time (using now()): {}'.format(datetime.datetime.now()))
print('Local time (using utcnow()): {}'.format(datetime.datetime.utcnow()))
print('-' * 100)
print()

print('----- USING PYTZ MODULE ------')
zone = 'Africa/Gaborone'
tz_to_display = pytz.timezone(zone)
local_time = datetime.datetime.now(tz=tz_to_display)
utc_time = datetime.datetime.utcnow()
print('Local time in {} is {}'.format(zone, local_time))
print('UTC time is {}'.format(utc_time))

for code in sorted(pytz.country_names):
    print('{} : {}'.format(code, pytz.country_names[code]))
