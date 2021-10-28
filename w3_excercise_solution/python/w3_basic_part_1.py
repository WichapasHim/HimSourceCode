
from os import environ


def item_3():
    import datetime as dt
    print(dt.datetime.now(tz=None))
    print(dt.datetime.now())


def item_4(r:float=0)->float:
    import math
    r=float(input())
    return math.pi*(r**2)


def item_5(first:str='',last:str='')->str:
    first_name=input()
    last_name=input()
    return '{} {}'.format(first_name[::-1],last_name[::-1])


def item_6():
    list_num=[int(i) for i in input().split(',')]
    tup_num=tuple(list_num)

    print(list_num,tup_num)


def item_7():
    file_name=input().split('.')
    return file_name[-1]
    

def item_8():
    color_list=['Red','Green','White','Black']
    return '{} {}'.format(color_list[0],color_list[-1])


def item_9():
    exam_st_date=(11,12,204)
    return '{} / {} / {}'.format(exam_st_date[0],exam_st_date[1],exam_st_date[2])


def item_10():
    n=input()
    return int(n)+int(n+n)+int(n+n+n)


def item_11():
    print(abs.__doc__)


def item_12():
    import calendar
    print(calendar.month(1996,7))


def item_14():
    import datetime
    date_1=datetime.date(2014,7,2)
    date_2=datetime.date(2014,7,11)
    return (date_2-date_1).days

def item_15():
    import math
    r=6
    return math.pi*(4/3)*(r**3)


def item_16():
    n=int(input())
    return (n-17)*2  if n>17 else 17-n


def item_18(a,b,c):
    if a==b==c: return 9*a
    return a+b+c


def item_19(s:str)->str:
    if s[0:2]=='ls' and len(s)>=2:return s
    return 'ls'+s


def item_20(s:str,n:int)->str:
    return s*n


def item_21():
    n=int(input())
    return '{} is even number'.format(n) if n%2==0 else '{} is odd number'.format(n)


def item_22(n:list)->int:
    count=0
    for i in n:
        if n==4:
            count+=1

    return count


def item_23(s:str,n:int)->str:
    if len(s)<2: return n*s
    return s[0:2]*n

def item_24(s:str):
    return s in 'aeiou'


def item_25(l:list,v:int):
    return v in l


def item_26(n:int)->str:
    for i in n:
        print('@'*i)


def item_27(l:list)->str:
    return ''.join([str(i) for i in l])


def item_28():
    numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
    for i in numbers:
        if i==237:break
        if i%2==0: print(i)


def item_29(set1,set2):
    return set1-(set1.intersection(set2))


def item_30(h,l):
    return 0.5*h*l


def item_31(a,b):
    gcd=0
    gcd_check= a if a<=b else b
    gcd_remain=a if a>b else b
    for i in range(1,gcd_check+1):
        if gcd_check%i==0 and  gcd_remain%i==0 and i>gcd:
            gcd=i

    return gcd











#4 12 --> 1 , 2 , 4


def lcm(a,b):
    i=min(a,b)
    while True:
        if i%a==0 and i%b==0:
            print(i)
            break
        else:
            i+=1


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head=ListNode([1,2,3,4],4)
























def item_32(a,b):
    starter=a if a>=b else b
    while True:
        
        if starter%a==0 and starter%b==0:
            return starter
        else:
            starter+=1

def item_33(a,b,c):
    if a==b  or b==c or a==c: return 0
    return a+b+c


def item_34(a:int,b:int)->int:
    return 20 if 15<=(a+b)<=20 else a+b


def item_35(a,b):
    return a==b or a-b==5 or a+b==5


def item_36(a:int,b:int)->int:
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    return "Not int"


def item_37(name:str,age:int , adress:str)->str:
    return 'Name : {}\nAge : {}\nAdress : {}'.format(name,age,adress)


def item_38(x:int,y:int)->int:
    return (x+y)**2


def item_39(amt:int=0,interest:float=0,years:int=0)->float:
    pass



def item_40(point_1:tuple,point_2:tuple)->float:
    return ((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)**(1/2)



def item_41():
    import os
    print(os.path.isfile('main.txt'))
    print(os.path.isfile('main.py'))


def item_42():
    import platform 
    import  struct
    print(platform.architecture()[0])
    print(struct.calcsize('P')*8)


def item_43():
    import os
    import platform
    print(os.name)
    print(platform.system())
    print(platform.release())

def item_44():
    import site
    print(site.getsitepackages())


def item_45_1():
    from subprocess import call
    call(['ls','-l'])


def item_45_2():
    import os
    print(os.system('ls -l'))


def item_46():
    import os
    print(os.path.realpath(__file__))

def item_47():
    import multiprocessing
    print(multiprocessing.cpu_count())


def item_48(s:str):
    return (float(s),int(float(s)))


def item_50():
    for i in range(10):
        print('*',end='')


def item_51():
    import cProfile
    def sum():
        print(1+2)
    cProfile.run('sum()')

def item_53():
    import os
    print('*'*80)
    print(os.environ)
    print('*'*80)
    print(os.environ['HOME'])
    print('*'*80)
    print(os.environ['PATH'])
    print('*'*80)

def item_54():
    import getpass
    print(getpass.getuser())


def item_57(n):
    import time
    start_time=time.time()
    sum=0
    for i in range(1,n+1):
        sum+=i
    end_time=time.time()
    
    return '{} takes {} '.format(sum,end_time-start_time)

def item_63(pad):
    import os
    print(os.path.abspath('pad'))
    
def item_65(times:float)->str:
    days=times//(24*3600)
    times=times%(24*3600)
    hours=times//(3600)
    times%=3600
    minutes=times//60
    seconds=times%60
    return '{} days {} hours {} minuts {} sec'.format(days,hours,minutes,seconds)


def item_66(kg:float=0,m:float=0)->float:
    return kg/(m**2)
    
    
def item_68(n:int)->int:
    sum=0
    while True:
        sum+=n%10
        n//=10
        if n==0 :break
        
    return sum


def item_69(a,b,c):
    pass



def item_72():
    import math
    print(dir(math))


def item_73(p_1:tuple=(0,0),p_2:tuple=(0,0))->tuple:
    return ((p_1[0]+p_2[0])/2,(p_1[1]+p_2[1])/2)


def item_75():
    import sys
    print(sys.copyright)
    

def item_78():
    help('modules')
    
def item_79(ob):
    import sys
    return sys.getsizeof(ob) #bytes


def item_80():
    import sys
    print(sys.getrecursionlimit())
    
def item_81(string_list:list=[])->str:
    return '-'.join(string_list)


def item_82(con):
    t=0
    if isinstance(con,dict):
        for i in con:
            t+=con[i]
            
        return t
    
    return sum(con)


def item_83(n_list,n):
    return all(i>n for i in n_list)


def item_84(s:str,f:str)->int:
    return s.count(f)


def item_87():
    import os
    file_size=os.path.getsize('interesting_excersie.txt')
    print(file_size)
    
    
def item_88(x:int=0,y:int=0)->str:
    return '{}+{}={}'.format(x,y,x+y)


def item_90(src,dest):
    with open(src)as f , open(dest,mode='w')as d:
        d.write(f.read())
        item_90('code.py','code2.py')
        with open('code2.py',mode='r') as filehandle:
            for line in filehandle:
                print(line,end='')


def item_91(a,b):
    a,b=b,a
    print(a)
    print(b)
    

def item_93(x):
    print('type of {}'.format(type(x)))
    print('id of {}'.format(id(x)))
    
    
def item_94(x):
    x=b'ABC'
    print(x)
    print(list(x))


def item_95(s:str)->bool:
    return s.isdigit()


def item_96():
    import traceback
    def add_bet():
        return check_stack()
    
    def check_stack():
        traceback.print_stack()
        
    add_bet()


def item_98():
    import time
    print(time.ctime())
    print(time.time())
    
    
    
def item_99():
    import os
    import time
    for i in range(5):
      os.system('cd')
      
    os.system('cls')
    

def item_100():
    import socket
    host_name=socket.gethostname()
    print(host_name)
    
    
def item_101():
    from http.client import HTTPConnection
    pass


def item_103():
    import os
    print(os.path.basename(''))#path goes here
    pass
    
    
def item_105():
    import os
    print(os.environ)
    
    
def item_107():
    import os.path
    import time

    print('File         :', __file__)
    print('Access time  :', time.ctime(os.path.getatime(__file__)))
    print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    print('Change time  :', time.ctime(os.path.getctime(__file__)))
    print('Size         :', os.path.getsize(__file__))
  
  
def item_109(n:float)->str:
    if n==0: return 'Zero'  
    if n<0:return 'Negative'
    if n>0:return 'Positive'
    
    
def item_110(n:int)->bool:
    return n%15==0


def item_112(l:list)->list:
    del l[0]
    return l



def item_113():
    while True:
        try:
            n=int(input('Enter number : '))
            break
        except ValueError:
            print('Error')
            
            
def item_114(l:list)->list:
    return [i for i in l if i>0]


def item_116():
    str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
    print()
    print(str)
    print()
    
    
def item_117(str_1:str='',str_2:str='')->bool:
    return id(str_1)==id(str_2)



def item_122():
    n = 20
    d = {"x":200}
    l = [1,3,5]
    t= (5,7,8)
    print(type(n)())
    print(type(d)())
    print(type(l)())
    print(type(t)())
    
    
def item_123():
    import sys
    print(sys.int_info)
    print()
    print(sys.float_info)
    print()
    print('Maxsize of integer : ',sys.maxsize)
    
    
def item_124(a,b,c)->bool:
    return a==b==c


def item_128(s:str)->bool:
    return any(i.islower() for i in s)


def item_137(dick:dict):
    return dick.items()


def item_138(b:bool)->int:
    return int(b)


def item_142():
    import os, platform
    print("Operating system name:")
    print(os.name)
    print("Platform name:")
    print(platform.system())
    print("Platform release:")
    print(platform.release())
    
    
def item_148(l:list)->tuple:
    max=l[0]
    min=l[0]
    for num in l:
        if num>max:
            max=num
        elif num<min:
            min=num
            
    return max,min

def item_149(n:int)->int:
    sum=0
    for i in range(n-1,0,-1):
        sum+=i**3
        
    return sum


                
                
                




    

    
    
    





    


   
        


    

    






        

