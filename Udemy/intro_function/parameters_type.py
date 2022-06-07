def func(p1,p2,*args,k,**kwags):
    print('positional-or-keyword {} {}'.format(p1,p2))
    print('var positional args {}'.format(args))
    print('keyword {}'.format(k))
    print('var-keyword {}'.format(kwags))
func(1,2,3,4,5,6,7,8,k=8,key1=555,key2='bet')