S="15:15:01"
start_time=3600*(int(S[0:2]))+60*(int(S[3:5]))+int(S[6:])
print(start_time)
h=0
m=0
s=0

h=start_time//3600
start_time=start_time%3600
m=start_time//60
start_time=start_time%60
s=start_time

time='{}:{}:{}'.format(h if len(str(h))!=1 else '0'+str(h),m if len(str(m))!=1 else '0'+str(m),s if len(str(s))!=1 else '0'+str(s))
print(time)