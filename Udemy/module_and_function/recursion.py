def fact_normal(n):
    result=1
    if n>1:
        for f in range(2,n+1):
            result*=f
    return result

def fact_recursive(n):
    if n<=1:
        return 1
    else:
        return n*fact_recursive(n-1)


def fibonanci(num):
    """F(n)=F(n-1)+F(n-2)"""

    if n<2:
        return num
    else:
        return fibonanci(num-1)+fibonanci(num-2)


def fibonanci2(num):
    if num==0:
        result=0
    elif num==1:
        result=1
    else:
        n_minus1=1
        n_minus2=0
        for f in range(1,num):
            result=n_minus2+n_minus1
            n_minus2=n_minus1
            n_minus1=result
    return result