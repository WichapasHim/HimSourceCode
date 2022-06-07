import datetime as dt
import pandas as pd



a='1/5/2018 6:00:14 AM'
import datetime
a=pd.to_datetime(a)
a=a.datetime.tz_localize('UTC')
print(a)



b=['a','b']
c=''.join(b)



d='0006A'
#e=int(d)
#print(e)
