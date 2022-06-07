def factorial(number:int)->int:
    """
    Calculate Factorial
    """
    if number==0:
        return 1
    fac_num=1
    for i in range(1,number+1):
        fac_num*=i

    return fac_num


def factorial_recursive(number):
    if number<=1:
        return 1
    
    return number*factorial_recursive(number-1)

for i in range(36):
    print(i,factorial(i))
    print(i,factorial_recursive(i))


