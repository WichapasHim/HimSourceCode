def item_1(l:list)->bool:
    return len(set(l))==len(l)


def item_2(): #ติดไว้ก่อน
   # pos_str=''
    
    shuf_a=[]
    for j in range(5):
        a=['a','e','i','o','u']
        shuf_a.append(a[j])
        a.pop(j)
        shuf_a+=a
        a=[]
        print(shuf_a)
        shuf_a=[]


       
            
def item_3(l:list):
    pop_index=0
    while len(l)!=0:
        pop_index=(pop_index+2)%len(l)
        print(l.pop(pop_index))
        


def item_4():#น่าสนใจแต่โจทไม่เคลียร์
    pass


def item_5(): #ไม่เข้าใจโจทย์
    pass


def item_6(s:str): #fix duplicate
    word_list=s.split()
    word_count=[word_list.count(n) for n in word_list]
    print(word_list)
    print(list(zip(word_list,word_count)))
    
    
def item_8():
    import bs4
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    # Print news title, url and publish date
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("-"*60)
        
        
        
def item_9():
    import pkg_resources
    pass

def item_11(target:int)->set:
    pass


def item_12():
    pass


def item_13(s:str)->list:
    string_maps = {
                    "1": "abc",
                    "2": "def",
                    "3": "ghi",
                    "4": "jkl",
                    "5": "mno",
                    "6": "pqrs",
                    "7": "tuv",
                    "8": "wxy",
                    "9": "z"
                    }
    result=[]
    for i in string_maps[s[0]]:
        for j in string_maps[s[1]]:
            add_s=i
            add_s+=j
            result.append(add_s)
            
    return result


def item_16(a:int=0,b:int=0,opposite_90:int=0)->float:
    if a==0:
        return (opposite_90**2-b**2)**(1/2)
    elif b==0:
        return (opposite_90**2-a**2)**(1/2)
    elif opposite_90==0:
        return (a**2+b**2)**(1/2)
    else:
        return 'You knew it'
    

def item_17(n:int=0)->list:
    strobogrammatic_number={'0':'0','1':'1','6':'9','8':'8','9':'6'}
    list_check_swap=[]
    if n==0:return []
    if n==1:return ['1','0','8']
    for i in range(10**(n-1),10**n):
        i=str(i)
        check_swap=''
        if len([j for j  in i if j in '23457'])==0:    #ความเท่อยุ่บรรรทัดดนี้    
            for key in strobogrammatic_number:
            
                for sing_num in i:
                    check_swap+=strobogrammatic_number[sing_num]
                    print(check_swap)
                if check_swap==i[::-1]:
                    list_check_swap.append(check_swap)
                    
                    
    return list_check_swap


def item_18(a,b,c):
    if a<=b<=c or c<=b<=a:return b
    if b<=a<=c or c<=a<=b:return a
    if b<=c<=a or a<=c<=b:return c



def item_19(n:str)->int:
    count=0
    i=1
    str_check=''
    while True:
        i*=2
        str_check+=str(i)
        print(str_check)
        count+=1
        if len(n)==len(str_check): break
        
    return count


def item_20(x):
    def factorial(n):
        if n==0:return 1
        if n==1:return 1
        return n*factorial(n-1)
    
    fac_val=factorial(x)
    count=0
    while True:
        if fac_val%10==0:
            count+=1
            fac_val/=10
            print(fac_val)
        else:    
            return count
    
    
def item_21(amount:int)->int:
    notes={'ten':10,'twenty':20,'fifthy':50,'hundred':100,'two-hundred':200,'five-hundred':500}
    notes_key=list(notes.keys())
    notes_value=sorted(list(notes.values()),reverse=True)
    count=0
    money_notes_need=[]
    while True:
        if len(str(amount))<2:break
        for money in notes_value:
            count+=amount//money
            money_notes_need.append((notes_key[notes_value.index(money)],amount//money))
            amount%=money
            print(amount)
            
    return money_notes_need,count


def item_23(n):
    count=0
    while n>0:
        sum_digit=sum([int(i) for i in str(n)])
        n-=sum_digit
        print(n)
        count+=1
        
    return count


def item_24(n:int)->int:
    return len([i for i in range(1,n+1) if n%i==0])

5
def item_25(phone_number:str)->list:
    set_phone_number=set(list(phone_number))
    whole_num=list('0123456789')
    for i in set_phone_number:
        if  i  in '0123456789' :
           whole_num.pop(whole_num.index(i))
            
    return whole_num


def item_26(l:list)->int:
    distinct_pairs_list=[]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            tupe_part=(l[i],l[j])
            distinct_pairs_list.append(tupe_part)
    print(distinct_pairs_list)     
    return sum([abs(i[0]-i[1]) for i in distinct_pairs_list]) #ความเท่อยุ่บรรทัดนี้


def item_27(l:list)->list:
    if len(l)<3 :return 'WTF'
    if l[1]==0:
        print('Wrong type')
        return None
    lek_kanit=list(set([l[i+1]-l[i] for i in range(0,len(l)-1)]))
    leka_kanit=list(set([(l[i+1]/l[i]) for i in range(0,len(l)-1)]))
    print(lek_kanit,leka_kanit)
    
    if len(lek_kanit)==1: 
        print('type : lekanit and nex val is {}'.format(l[-1]+lek_kanit[0]))
    elif len(leka_kanit)==1:
        print('type : lekakanit and next val is {}'.format(l[-1]*leka_kanit[0]))
    else:
        print('Wrong type')
        

def item_28(l:list):
    third_term=l[2]
    last_third_term=l[-3]
    length=len(l)
    sum_l=sum(l)
    print(third_term,last_third_term,length,sum_l)
    
    
def item_29(a:int=1,b:int=1)->int:
    less_num=a if a<b else b
    more_num=a if a>b else a
    gcd=1
    count=1
    for i in range(2,less_num+1):
        if less_num%i==0 and more_num%i==0 and i>gcd:
            gcd=i
            count+=1
    return count


def item_30(n:int=0)->int:
    sum_swap=n
    while True:
        
        n_swap=int((str(sum_swap))[::-1])
        print(n_swap)
        sum_swap=sum_swap+n_swap
        print(sum_swap)
        if str(sum_swap)==str(sum_swap)[::-1]: 
            return sum_swap
            break
        

def item_31(a,b):
    total,n,tod,carry=0,0,0,[]
    while True:
        sed=((a%10)+(b%10)+tod)%10          #2  5   3 
        tod=((a%10)+(b%10)+tod)//10         #1  1   1 
        carry.append(tod)                   #[1]   [1,1]  [1,1,1]
        total=total+(sed*(10**n))           #2  52      352
        a//=10                              #56  5      0
        b//=10                              #78  7      0
      
        n+=1                                #1   2      3
        if a==0 or b==0:
            total+=(tod*(10**n))
            break
        
    return len(carry),total



def item_32()->list:
    return (sorted([int(input()) for i in range(8)],reverse=True))[:3]


def item_33(a:int=0,b:int=0)->int:
    sum=a+b
    if sum==0: return 1
    digit_count=0
    while sum>0:
        sum//=10
        digit_count+=1
        
    return digit_count


def item_34():
    pass


def item_35(a,b,c,d,e,f)->tuple:
    if not(all(-1000<=i<=1000 for i in [a,b,c,d,e,f])): return 'Out of range'
    x=(f-e*c/b)/(d-a*e/b)
    y=(c-a*x)/b
    return x,y
    """y=((c-ax)/b)
    x=(c-by)/a
    dx+(e*((c-ax)/b))=f
    dx+(e/b)*(c-ax) =f
    dx+(ec/b)-(axe/b)=f
    x(d-ae/b)=f-ec/b
    x=(f-ec/b)/(d-ae/b)"""
    
    
def item_37(n:int=0)->int:
    if not(1<=n<=50):return 'out of range'
    count=0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for w in range(10):
                    if i+j+k+w==n:
                        count+=1
                        
    return count


def item_38(k):
    def is_prime(n):
        if n<=1: return False
        if n==2:return True
        count=0
        for i in range(2,n):
            if n%i==0:count+=1
                
        return count==0 
    prime_count=0
    for i in range(k):
        if is_prime(i):prime_count+=1
            
    return prime_count



def item_39()->tuple:
    cor=[tuple([int(i) for i in input().split()]) for i in range(3)] #nest list comprehension
    #the rest of code is so math ----> skippp (but the main point in coding is nested list comprehension)
    pass


def item_40():
    #โจทย์ งงจัด 
    pass


def item_41(a,b):
    return 'overflow' if a+b>(10**80) else ('Negative or zero'  if  a+b<=0 else a+b)
    

def item_42():
    x=[int(i) if -100000<=int(i)<=100000 else 'Error' for i in input().split()]
    if 'Error' in x : return 'Out of range'
    return sorted(x,reverse=True)


def item_43():
    line_1=[tuple([int(k) for k in input().split()]) for i in range(2)]
    line_2=[tuple([int(k) for k in input().split()]) for i in range(2)]
    return (line_1[0][1]-line_1[1][1])/(line_1[0][0]-line_1[1][0])==(line_2[0][1]-line_2[1][1])/(line_2[0][0]-line_2[1][0])


def item_44():
    print('Input number of sequence of numbers you wanna input (0 to exit): ')
    n=int(input())
    if n==0:return None
    sum,count=0,0
    print('Input numbers : ')
    while True:
        k=int(input())
        if n==0:break
        sum+=k
        count+=1
        if count==n:
            print('Maximum sum of the said contigous subseqeunce : ')
            print(sum)
            print('Input number of sequence of numbers you wanna input (0 to exit): ')
            n=int(input())
            if n==0:break
            print('Input numbers : ')
            count,sum=0,0
            
    
    
def item_45():
    x1,y1,r1,x2,y2,r2=[int(i) for i in input().split()]
    dis_cen=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
    r_tot=r1+r2
    if dis_cen>r_tot:return 'Not overlap'
    if dis_cen==r_tot:return 'touch'
    if dis_cen<r_tot:
        if dis_cen+r1<r2: 
            return 'C1 in C2'
        elif dis_cen+r2<r1:
            return 'C2 in C1'
        else :
            return 'Intersect'
        
        
def item_47():
    n=input().split()
    set_word=set(n)
    dict_word_count={ i:0 for i in set_word} #first time using short expression with dictionary
    for word in set_word:
        dict_word_count[word]+=n.count(word)
        
    return ('common word : {}'.format(([k for k in dict_word_count if dict_word_count[k]==max(list(dict_word_count.values()))])[0]),'max_char : {}'.format(([k for k in list(dict_word_count.keys()) if len(k)==max([len(i) for i in list(dict_word_count.keys())])])[0]))   #Bad code



def item_48():
    #Confuse problem
    pass
    
    
def item_49(a,b,c):
    return a**2+b**2==c**2



def item_50(n):
    n=n.split()
    swap_word={'Python':'Java','Java':'Python'}
    for index,word in enumerate(n):
        if word in swap_word:
            n[index]=swap_word[word]
            
    return ' '.join(n)


def item_51(n:int=0)->int:
    n=str(n)
    return int(''.join(sorted([i for i in n],reverse=True)))-int(''.join(sorted([i for i in n]))) #sorted string?????


def item_52(x):
    def is_prime(n):
        if n<=1:return False
        if n==2:return True
        check_prime=0
        for i in range(2,n):
            if n%i==0:
                check_prime+=1
                
        return check_prime==0
    count_prime,num,sum=0,0,0
    while count_prime!=x:
        if is_prime(num):
            count_prime+=1
            sum+=num
        num+=1
        
    return count_prime,sum


def item_53():
    pass



    
        
    










   
    

    








    
    
    
    

    
    



    



    
    



    



    

    







    

 
    
    


            


    