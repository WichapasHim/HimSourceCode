import math

"""def item_1()->int:
    hour,min,sec=[int(i) for i in input().split(',')]
    return hour*3600+min*60+sec

print(item_1())"""


"""def item_2()->int:
    x=int(input())
    return 2-x+(3/7*x**2)-(5/11*x**3)+math.log(x,10)"""


"""def item_3()->float:
    a=float(input())
    for i in range(4):
        x=(x+a/x)/2
    return x"""


"""def item_4()->float:
    v1,v2,v3=[float(i) for i in input().split()]
    u1,u2,u3=[float(i) for i in input().split()]
    return v1*u1+v2*u2+v3*u3"""


"""def item_5()->float:
    x1,y1,x2,y2=[float(i) for i in input().split()]
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)"""


"""def item_8()->float:
    a,b,c,d,e=[float(i) for i in input().split()]
    return (a+b+c+d+e)/5"""


"""def item_9()->str:
    a,b,c=[i for i in input().split()]
    c=int(c)
    return a+b+str(c)+((a+b)*c)"""


"""def isbn():
    num=input()
    isbn_num_9=0
    mul=10
    for i in range(len(num)):
        isbn_num_9+=int(num[i])*mul
        mul-=1
        print(isbn_num_9)
    return num+str(11-(isbn_num_9%11))"""




