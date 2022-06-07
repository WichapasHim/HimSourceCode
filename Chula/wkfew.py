def reverse(self, x: int) -> int:
    if not(-2**31<=x<=2**31-1) : return 0
    check_minus=0
    if x<0: 
        check_minus+=1
        x*=-1
    x=str(x)
    re_x=x[::-1]
        
    if check_minus==0:
        return int(re_x)
    else:
        return int(re_x)*(-1)

