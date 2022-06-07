"""
item_1
Ans 1.1 : Dict
Ans 1.2

"""

def item_2(x):
    return tuple([i for i in range(0,x) if i%2==0])


def item_3(x):
    return tuple([int(i) for i in x])

def item_4(x):
    dick={}
    for i in x:
        if i not in dick:
            dick[i]=1
        else:
            dick[i]+=1

    return dick

def item_5(x='',y=''):
    x=set((' '.join(x)).split())
    y=set((' '.join(y)).split())
    print(x,y)
    print(x.intersection(y))



def item_6():
    n=int(input())
    stu_info={}
    for i in range(n):
        info=input().split()
        if info[1] not in stu_info:
            stu_info[info[1]]=set(info[0:1])
        else:
            stu_info[info[1]].add(info[0])

    find_faculty=[i for i in input().split()]
    print(stu_info)
    name_found=''
    for i in find_faculty:
        name_found+=' '.join(stu_info[i])+' '
    
    name_found=set((name_found.strip()).split())
    return ' '.join(name_found)



def item_7():
    n=int(input())
    set_list=[]
    for i in range(n):
        set_input=set([int(i) for i in input().split()])
        set_list.append(set_input)
 
    union_set=set([])
    intersect_set=set_list[0]
    for i in set_list:
        union_set=union_set.union(i)
        intersect_set=intersect_set.intersection(i)
        
    return len(union_set),len(intersect_set)


def item_8(n):
    n=int(input())
    word_list=[]
    word_dict={}
    for i in range(n):
        word=input().split('\t')
        word_list.append(word)

    for letter_list in word_list:
        if letter_list[1][0:2] not in word_dict:
            word_dict[letter_list[1][0:2]]=1
        else:
            word_dict[letter_list[1][0:2]]+=1
 
    keen=list(word_dict.keys())
 
    word_firstwo=[]
    for i in keen:
        word_firstwo.append([i,word_dict[i]])
    word_firstwo=sorted(word_firstwo)
    for i in range(len(word_firstwo)-1,-1,-1):
        if word_firstwo[i][1]!=word_firstwo[0][1]:
            word_firstwo.pop(i)
    print(word_firstwo[0][0])
    print(word_firstwo[0][1])
    for index,value in enumerate(word_list):
        if word_firstwo[0][0] in value[1]:
            print(value[1],value[0])
    










item_9()




def item_9():
    stu_info={}
    while True:
        n=[i for i in input().split()]
    
        if n[0]=='-1': break
        stu_info[n[0]]=set(n[1:])

    #return stu_info
    subject_check=set([i for i in input().split()])
    count_both=0
    count_once=0
    for index,value in enumerate(stu_info):
        if len(subject_check)==len(stu_info[value].intersection(subject_check)):
            count_both+=1
        elif len(stu_info[value].intersection(subject_check))>0:
            count_once+=1

    return count_both,count_once,count_once+count_both













        

    
    


    




    













    


    










     
