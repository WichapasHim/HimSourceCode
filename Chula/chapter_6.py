def item_1()->float:
    v1=[int(e) for e in input().split()]
    v2=[int(e) for e in input().split()]

    if len(v1)!=len(v2): return 'Error'
    dot=0
    for i in range(0,len(v1)):
        dot+=v1[i]*v2[i]

    return dot



def item_2(n:int=0):
    n=int(input())
    b=[]
    for i in range(n):
        x=input()
        b.append(x)

    return ','.join(b)


def item_3(n):
    bg=['G' if i<n else 'B' for i in range(2*n)]
    d=1
   
    return None

def item_4(r,c):
    matix=[]
    for i in range(r):
        matrix_sub=[int(i) for i in input().split()]
        if len(matrix_sub)==c:
            matix.append(matrix_sub)
        else:
            matix.append([])

    return matix

def item_5():
    n=int(input())
    acc=[]
    for i in range(n):
        s=input()
        acc.append((len(s),s))
    
    return sorted(acc)
    

def item_6():
    n,m=[int(i) for i in input().split()]
    score_list=[]
    error_check=[]
    for i in range(n):
        student_list=[int(value) if index!=0 else value  for index,value in enumerate(input().split())]
        if len(student_list)-1 !=m : error_check.append(student_list[0])
        score_list.append([sum(student_list[1:]),student_list[0]])
        score_list=sorted(score_list)
        score_list.reverse()
        
    print(score_list)


    if len(error_check)!=0:
        print('Invalid data')
        for i in error_check:
            print(i)
    else:
        for i in score_list:
            print('{} {}'.format(i[1],i[0]))


  

    

    

      

    






    




    










