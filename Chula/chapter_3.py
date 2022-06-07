#Multiple of 3 or 5
"""def multiple_of_three_or_five(num:int=0)->int:
    num=int(input())
    check_threefive=0
    sum=0
    while  check_threefive<num:
        if check_threefive%3==0 or check_threefive%5==0:
            sum+=check_threefive
            
        check_threefive+=1
    return sum"""


"""def item_1()->int:
    k=1
    while (k*(1/k))==1:
        k+=1
    return k"""


"""def item_2()->int:
    k=1
    n=1.0
    
    while 1-n<0.5:
        k+=1
        n*=(365-k)/365
    return k



def item_2_chula():
    k=1
    p=1.0
    while (1-p)<0.5:
        p*=(365-k)/365
        k+=1
    
    return k

print(item_2())
print(item_2_chula())"""



"""def item_3()->float:
    k=1
    mul=3
    i=1
    while mul<=399999:
        k+=(((-1)**i)*(1/mul))
        i+=1
        mul+=2

    return 4*k

print(item_3())   """

"""def item_3_chula():
    p=0
    for k in range(1,400000,4):
        p+=1/k
        p-=1/(k+2)
    return 4*p"""

"""
def item_4(a:int,b:int)->float:
    sum1=0
    for i in range(a,b):
        sum2=0
        for j in range(a+1,b+1):
            sum2+=i+j
        sum1+=((-1)**i)*sum2

    return sum1"""

"""def item_6()->int:
    n=int(input())
    neg=0
    max=n
    min=n
    for i in range(n):
        num=int(input())
        if num<0: neg+=1
        if num>max:max=num    
        if num<min: min=num    
    return (max-min,neg)

print(item_6())"""


"""def item_7():
    n=int(input())
    
    for ix in range(1,n+1):
        for iy in range(1,n+1):
            for iz in range(1,n+1):
                print(ix**2+iy**2+iz**2,ix,iy,iz)

print(item_7())"""
           
"""def item_8(x:int)->float:
    def factorial(n):
        if n<=1:
            return 1
        return n*factorial(n-1)
    k=0
    sin_x=0
    count=1
    while count*(1/count)==1:
        sin_x+=((-1)**k)*(x**((2*k)+1))/(factorial(2*k+1))
        k+=1
        count+=1

    
    return sin_x

print(item_8(45))"""



"""def item_8()->float:
    sum=0
    count=0
    while True:
        num=int(input())
        if num==-1: 
            if count==0:
                return 'No data'
            break
            
        sum+=num
        count+=1

    return sum/count

print(item_8())"""


#needs improve (reduce loop range)
"""def tri_90_degree()->int:
    perimeter=int(input())
    z=peta=0
    for x in range(perimeter//2):
        for y in range(perimeter//2):
            
            z=(x**2+y**2)**(1/2)
            if x+y+z==perimeter:
                peta=z
            print('x:{} , y:{} , z:{} , peta:{}'.format(x,y,z,peta))

tri_90_degree()"""



    









    

    






        




        
