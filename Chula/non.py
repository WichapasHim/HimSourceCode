from typing import Hashable


number_1=10
number_2=20

total=number_1+number_2

#print('Number 1 : ' +str(number_1))

#   Number 1 : 10  , Number 2 : 20  , Then Number 1 plus Number 2 : 30
#print('Number 1 : '+str(number_1)+' , '+'Number 2 : '+str(number_2)+' , '+'Then Number 1 plus Numner 2 : '+str(number_2+number_1)) 

#F-String Python 3.6+++++
string_total=f'Number 1 : {number_1} , Number 2 : {number_2} , Then Number 1 plus Number 2 : {number_1+number_2}'
#print(string_total)


#String Format 
#print('Number 1 : {} , Number 2 : {} , Then Number 1 plus Number 2 : {}'.format(number_1,number_2,number_1+number_2))


#Expression , Statement
#สร้างลิสต์ที่ มีตัวเลขอยุ่ในช่วง 0,20 เป็นเลขคู่
list_even_1=[0,2,4,6,8,10,12,14,16,18,20]
#print(list_even_1)


list_even_2=[]
#range(start=0,stop,step=1)
for i in range(21):
    if i%2==0:
        list_even_2.append(i)

#print(list_even_2)

list_even_3=[]
for i in range(0,21,2):
    list_even_3.append(i)

##print(list_even_3)

#iterable object

#best
list_even_4=list(range(0,21,2))
#print(type(range(21)))
#print(list_even_4)


#List comprehension
list_even_5=[i for i in range(0,21,2)]


init_list=['a','b','c','d','e',1,2,3,4,5]

#สร้างlist ใหม่ที่บรรจุ แค่ value ที่indexเป็นเลขคู่
even_index=[]
for i in range(0,len(init_list),2): #0 2 4 6 8
    even_index.append(init_list[i])

#print(even_index)


#even_index=[init_list[i] for i in range(0,len(init_list),2)]



for i in range(10):
    pass #0 1 2 3 4 5 6 7 8 9


"""
init_list=['a','b','c','d','e',1,2,3,4,5]
for i in init_list: 
    print(i)


print() 


for i in range(0,len(init_list),1):
    print(init_list[i])"""



#Unpacklist

a,b,c=[1,2,3]


a='a b c'.split()
#x=input()

#x=input().split()


#ให้ input ตัวเลข 3 ตัวเก็บในตัวแปร ชื่อ x,y,z ใน1 บรรทัด เว้นวรรคด้วย ช่องว่าง
#x,y,z=[int(i) for i in input().split()] 
# 1.   '1 2 3'
# 2.   ['1','2','3']
# 3.   i='1'   , i='2'   ,i='3'
# 4.   append(int(i))
# 5. [1,2,3]
# 6. x,y,z=[1,2,3]


#ให้ vector 3 มิติ 2 ตัว หาผล dot vector   (x1,y1,z1)    (x2,y2,z2)
#vector 1 
#x1,y1,z1,x2,y2,z2=[int(i) for i in input().split()] # 1 2 3 4 5 6








#Enumerate function

a='abcdefg'

for i in a:
    print(i)

print()

for i in range(len(a)): # for i in range(6)
    print(i,a[i])

print()
for haha,bbbb in enumerate(a): #(0,'a')  ->  (1,'b')
    print(haha,bbbb)













