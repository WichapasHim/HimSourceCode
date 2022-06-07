import math


"""def item_1(x:int=0,y:int=0,z:int=0)->int:
    x,y,z=[int(i) for i in input().split()]
    if x<y<z or z<y<x:
        return y
    elif y<x<z or z<x<y:
        return x
    else:
        return z"""


"""def item_2()->str:
    h1,k1,r1=[float(i) for i in input().split()]
    h2,k2,r2=[float(i) for i in input().split()]
    distance_center=((h1-h2)**2+(k1-k2)**2)**(1/2)
    distance_radius=r1+r2
    if distance_center==distance_radius:
        return 'touch'
    elif distance_center<distance_radius:
        return 'overlap'
    else:
        return 'free'"""


"""def item_3()->str:
    x,y=[float(i) for i in input().split()]
    if x==0 and y==0: return 'origin'
    if x>0:
        if y>0: return 'Q1'
        if y<0: return 'Q4'
    if x<0:
        if y>0: return 'Q2'
        if y<0 :return 'Q3'"""

    
"""def item_4()->bool:
    a,b,c,d,e=[float(i) for i in input().split()]
    return a<=b<=c<=d<=e"""

"""
def item_5()->int:
    a=[float(i) for i in input().split()]
    min=0
    max=0
    for index,value in enumerate(a):
        if value<min:
            min=value
        if value>max:
            max=value
    
    return sum(a)-min-max"""


"""def item_6(a:int)->str:
    return 'Has' if a==(round(a**(1/3),0))**3 else 'No'

print(item_6(25))"""


"""def item_7(breast:int)->str:
    if breast<37:
        return 'XS'
    elif 37<=breast<41:
        return 'S'
    elif 41<=breast<43:
        return 'M'
    elif 43<=breast<46:
        return 'L'
    else:
        return 'XL'"""





    
    





    
