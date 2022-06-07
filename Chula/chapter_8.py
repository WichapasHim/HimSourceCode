def f1(a:str,b:int)->None:
    for i in range(b):
        print(a)


def f2(a:str,b:int)->list:
    return [a]*b

def g(m,b,n,c):
    if m==n and b!=c:return 1
    if m==n and  b==c: return 2
    x=(b-c)/(n-m)
    return x,(m*(x))+c


def h(x:list)->list:
    return [i for i in x if i%2==0]

def recur(n):
    if n==0:return 1
    if n==1:return -2
    return recur(n-2)*n

def super_recursive(n):
    if n==0: return 1
    if n==1: return 2

    if n%2==0:
        x=super_recursive(x/2)
        return x+(x%10)

    if n%2!=0:
        return super_recursive((n-3)/2)*((n-1)/2)


def s(i,k):
    if i>=k:return 0
    return k+t(i+1,k)

def t(j,k):
    if j>=k:return 0
    return j+s(j,k-1)





#Function Refactoring
def is_leap_year(y:int)->bool:
    return y%4==0 and (y%100!=0 or y%400==0)

def days_in_year(y:int)->int:
    return 365 if is_leap_year(y) else 366

def day_of_year(d:int,m:int,y:int)->int:
    d_m=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(y):
        d_m[1]+=1
    for i in range(m-1):
        d+=d_m[i]

    return d

def cal_date_diff():
    d1,m1,y1=[int(i) for i in input().split()]
    d2,m2,y2=[int(i) for i in input().split()]

    date_val_a=(day_of_year(d1,m1,y1),days_in_year(y1)) # not necessary just easy to read
    date_val_b=(day_of_year(d2,m2,y2),days_in_year(y2))
    date_durr_y=0
    for i in range(y1+1,y2):
        date_durr_y+=days_in_year(i)
    return (date_val_a[1]-date_val_a[0])+date_val_b[0]+date_durr_y 




#Four function
def make_int_list(x):
    return x.split()


def is_odd(e):
    return e%2!=0


def odd_list(alist):
    return [i for i in alist if i%2!=0]

def sum_square(alist):
    sum=0
    for i in alist:
        sum+=i**2
    return sum




def c_n_k(n:int,k:int):
    if 0<k<n: return c_n_k(n-1,k)+c_n_k(n-1,k-1)
    if k==0 or n==k : return 1
    return 0




#Recursive SumList
def sumlist(x:list)->int:  #ทำไงวะะะะะ
    pass 




    











