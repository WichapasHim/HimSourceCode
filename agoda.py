def centuryFromYear(year):
    return (year//100)+1 if year%100!=0 else year//100

def checkPalindrome(inputString):
    return inputString==inputString[::-1]

def adjacentElementsProduct(inputArray):
    
    ans=inputArray[0]*inputArray[1]
    for i in range(1,len(inputArray)-1):
        if inputArray[i]*inputArray[i+1]>ans:
            ans=inputArray[i]*inputArray[i+1]
            
    return ans


def shapeArea(n):
    if n==1:return 1
    core=(n*2)-1
    count=core
    while core!=1:
        count+=(core-2)*2
        core-=2   
    return count


def makeArrayConsecutive2(statues):
    statues.sort()
    max_num=statues[-1]
    ratiorg=[]
    for i in range(min(statues),max_num+1):
        if i==max_num:break
        if i not in statues:
            ratiorg.append(i)
            
    return len(ratiorg)
set_key={'a','b'}      
dict_s={}
for i in set_key:
    dict_s[i]=(0,0)
    
for i in dict_s:
    print(i)