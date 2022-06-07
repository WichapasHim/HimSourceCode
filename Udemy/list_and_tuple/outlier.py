#data=[4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
#data=[104,105,110,120,130,130,150,160,170,183,185,187,188,191]
#data=[104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
#data=[4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191]
#data=[1047,1051,11101,1201,1301,1501,1607,1831]
data=[]
"""del data[0:2]
print(data)
del data[-1:-3:-1]
print(data)"""

min_valid=100
max_valid=200

#process the low value in te list
stop=0
for index,value in enumerate(data):
    if value>=min_valid:
        stop=index
        break

print(stop)
del data[:stop]
print(data)


#process the high value in the list
start=0
for index in range(len(data)-1,-1,-1):
    if data[index]<=max_valid:
        start=index+1
        break
print(start)
del data[start:]
print(data)
