"""def item_1(s:str)->str:
    double_s=''
    for i in s:
        double_s+=(i*2)
    return double_s"""

"""def item_2(s:str)->str:
    print(len(s))
    s=' '+s+' '
    double_s=''
    for i in range (1,len(s)-1):
        double_s+=s[i]
        if s[i-1]!=s[i]!=s[i+1]:
            double_s+=s[i]
    print(len(double_s))
    return double_s"""   #Bug if has space
    
def item_3(s:str)->str:
    return s==s[::-1]

def item_6(s:str)->int:
    odd=0
    for letter in s:
        if letter in '13579':
            odd+=1
    return odd



def item_7(s:str)->str:
    months={1:'JAN',2:'FEB',3:'MAR',4:'APR',5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    return '{0} {1} {2}'.format(s[3:5],months[int(s[0:2])],s[6:])
    

def item_8(s:str)->str:
    count=0
    for letter in s:
        if letter.isupper():
            count+=1

    return count

def item_9(s:str)->str:
    check=0
    count=0
    for letter in s:
        if letter in 'aeiou':
            check+=1
        else:
            if check!=0:
                count+=1
    if s[-1] in 'aeiuo':
        count+=1
    return count

print(item_9('rythm'))











        
        




