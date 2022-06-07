def fizz_buzz(num:int)->str:
    """
    Fizz buzz function
    """
    if num%15==0:
        return 'fizz buzz'
    elif num%3==0:
        return 'fizz'
    elif num%5==0:
        return 'buzz'
    else:
        return str(num)


for i in range(1,101):
    print(fizz_buzz(i))