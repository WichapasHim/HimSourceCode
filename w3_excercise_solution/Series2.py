import pandas as pd


def item_1(a:list):
    ds=pd.Series(a)
    print(ds)
    
    
def item_2(a:list):
    ds=pd.Series(a)
    print(ds)
    print(type(ds))
    ds=ds.tolist()
    print(ds)
    print(type(ds))



def item_3(a:list,b:list):
    ds1=pd.Series(a)
    ds2=pd.Series(b)
    
    print(ds1+ds2)
    print(ds1-ds2)
    print(ds1*ds2)
    print(ds1/ds2)


def item_4(a:list,b:list):
    ds1=pd.Series(a)
    ds2=pd.Series(b)
    print(ds1==ds2)
    print(ds1>ds2)
    print(ds1<ds2)
    
    
def item_5(a:dict):
    ds=pd.Series(a)
    print(ds)
    
    
def item_6(a:list):
    import numpy as np
    b=np.array(a)
    ds=pd.Series(b)
    
    print(b)
    print(ds)


def item_7(a:list):
    ds=pd.Series(a)
    ds=pd.to_numeric(ds,errors='coerce')    
    
    print(ds)
    

def item_8():
     pass
 
 
    

