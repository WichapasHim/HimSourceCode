def cal_condo(price,pon):
    count=0
    while count<48:
        interest_monthly=price*0.02154/12
        print(interest_monthly)
        price=price-(pon-interest_monthly)
        count+=1
        
    return price
#cal_condo(2854660,40000)
print('Month : '+str(cal_condo(2854660,58000)))

def 