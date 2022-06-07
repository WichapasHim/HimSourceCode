import time
"""print(time.gmtime(0))

time_here=time.localtime()
print(time_here)
print('Year:',time_here[0],time_here.tm_year)
print('Month:',time_here[1],time_here.tm_mon)
print('Day:',time_here[2],time_here.tm_mday)"""


"""from time import process_time as my_timer
import random

input('Press enter to start')

wait_time=random.randint(1,6)
time.sleep(wait_time)
start_time=my_timer()
input('Press enter to stop')

end_time=my_timer()

print('Start at '+time.strftime('%X',time.localtime(start_time)))
print('Ended at '+time.strftime('%X',time.localtime(end_time)))
print('Your reaction time was {} seconds'.format(end_time-start_time))"""





"""print('The epoch in this system start at '+time.strftime('%c',time.gmtime(0)))

print('The current timezone is {} with an offset of {}'.format(time.tzname[0],time.timezone))


if time.daylight!=0:
    print('\tDaylight Saving Time is in effect fot this location')
    print('\tThe DST Timezone is '+time.tzname[1])


print('Local time is '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print('UTC time is '+time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))"""


"""import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())"""



import pytz
import datetime

country='Europe/Moscow'

tz_to_display=pytz.timezone(country)
local_time=datetime.datetime.now(tz=tz_to_display)

print('The time in {} is {}'.format(country,local_time))
print('UTC is {}'.format(datetime.datetime.utcnow()))

for x in sorted(pytz.country_names):
    print(x + ": "+pytz.country_names[x])