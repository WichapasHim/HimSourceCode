import pandas as pd
import numpy as np

def item_1():
    df=pd.Series([1,2,3,4])
    print(df)
  
  
def item_2():
    df=pd.Series([1,2,3,40])
    print(df)
    print(type(df))
    df=df.tolist()
    print(df)
    print(type(df))  
   
   
def item_3():
    df1=pd.Series([1,2,3,4])
    df2=pd.Series([1,2,3,4])
    print("""plus : {} 
             subtraction: {}
             multiplication : {}
             divide : {}""".format(df1+df2,df1-df2,df1*df2,df1/df2))
                 

def item_4():
    ds1 = pd.Series([2, 4, 6, 8, 10])
    ds2 = pd.Series([1, 3, 5, 7, 10])
    print(ds1==ds2)
    print(ds1>ds2)
    print(type(ds1<ds2))
    
    
def item_5():
    df=pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800})    
    print(df)


def item_6():
    num_array=np.array([1,2,3,3,4])
    ds=pd.Series(num_array,index=['A','B','C','D','E'])
    print(num_array)
    print(ds)


def item_7():
    ds=pd.Series(['100','200','python','300.12','400'])
    ds=pd.to_numeric(ds,errors='coerce')   #errors='coerce' ใส่เพราะ python ไม่สามารถ แปลงเป็น numericได้ ---> ไว้ fill NaN instead of get error ถ้าไม่ใส่จะแปลงไม่ได้
    print(ds)
    
    
    
def item_8():
    data_set=[[1,2,3,4,7,11],[4,5,6,9,5,0],[7,5,8,12,1,11]]
    d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
    df=(pd.DataFrame(data_set,index=['col1','col2','col3'])).transpose()
    df2=pd.DataFrame(data=data_set)
    df3=pd.DataFrame(d)
    ds=df['col1']
    print(df)
    print(ds)
    print(df2)
    print(df3)



def item_9():
    ds=pd.Series(['100','200','python','300.12','400'])
    ds_list=ds.to_list()
    print(ds_list)
    ds_array=np.array(ds_list)
    print(ds_array[0])
    ds_toooo_array=np.array(ds)#convert จาก Seires เป็น ndarray ตู้มเดียวก็ได้นิหว่า  
    print(ds_toooo_array)
    
    

def item_10():
    ds=pd.Series([['Red','Green','White'],['Red','Black'],['Yellow']])
    print(ds)
    new_ds=[]
    for i in ds:
        for k in i:
            new_ds.append(k)
            
    new_ds=pd.Series(new_ds)
    print(new_ds)
  
    
def item_11():
    ds=pd.Series(['100','200','python','300.12','400'])
    ds=ds.sort_values()
    print(ds)
   
   
   
def item_12():
    ds=pd.Series(['100','200','python','300.12','400'])
    ds=ds.append(pd.Series([500,'php']))
    print(ds)
    
    
def item_13():
    ds=pd.Series([0,1,2,3,4,5,6,7,8,9,10])
    ds_condition=ds[ds<6]
    print(ds_condition)
    

def item_14():
    ds=pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
    print(ds)
    ds=ds.reindex(index=['B','C','A','E','D'])
    print(list(ds.index))
    print(list(ds))


def item_15():
    ds=pd.Series([1,2,3,4,5,6,7,8,9,5,3])
    mean_ds=ds.mean()
    print(mean_ds)
    std_ds=ds.std()
    print(std_ds)


def item_16():
    ds1=pd.Series([1,2,3,4,5])
    ds2=pd.Series([2,4,6,8,10])
    print(ds1.append(ds2))
    print(ds1[~(ds1.isin(ds2))])   #ไอตัวหนอน สำคัญมาก
    print(ds1[pd.Series(not(i) for i in (ds1.isin(ds2)))]) #วิธีแบบ เบสิค ไม่ใช้Method หรือไรแปลกๆ ทั้งนั้น 
    #print(type(ds1.isin(ds2)))
    #ds3=pd.Series(i for i in 'ABCD')
    #print(ds3)
    #test_ds=pd.Series(ds1.isin(ds2))
    #h=pd.Series([i for i in ds1.isin(ds2)])
    #print(~test_ds)
    #print(h)
    #for i in test_ds:
      #  print(i)

def item_17():
    ds1=pd.Series([1,2,3,4,5])
    ds2=pd.Series([2,4,6,8,10])
    
    #Him solution 1
    new_ds=ds1[~(ds1.isin(ds2))].append(ds2[~(ds2.isin(ds1))])
    print(new_ds)
    
    #Him solution 2
    new_ds_2=ds1[pd.Series(not(i) for i in ds1.isin(ds2))].append(ds2[pd.Series(not(i) for i in ds2.isin(ds1))])
    print(new_ds_2)
    
    #W3 solution
    
    
    
def item_18():
    num_state=np.random.RandomState(100)
    print(num_state)
    num_series=pd.Series(num_state.normal(10,4,20))
    print(num_series)
    result=np.percentile(num_series,q=[0,25,50,75,100])
    print(result)
    
    
    
def item_19():    
    ds=pd.Series(np.random.randint(3,size=10))
    print(ds)
    print(ds.value_counts()) #method นี้ดี
    
    
def item_20():
    ds=pd.Series(np.random.randint(3,size=14))
    #print(ds)
    #print(type(ds.value_counts()))
    #print(ds.value_counts())
    #print(ds.value_counts()[0])
   # print(type(ds.value_counts()[0]))
    #print(ds.value_counts().index[:1])
    #print(type(ds.value_counts().index[:1]))
    #ds1=pd.Series([1,2,3,4])
    #ds2=pd.Series([2,3,5,6])
    #print(ds1[ds1.isin(ds2)])
    #print(ds1)


    #w3solution
    #ds[~ds.isin(ds.value_counts().index[:1])] ='other'  #does not work
    #print(ds)
    #ds[~ds.isin(ds.value_counts().index[:1])]
    print(ds)



    """result=ds
    for i in range(len(result)):
        print(i)
        if result[i]!=ds.value_counts().index[0]:
            result[i]='Other'
    
            
    print(result)
    print(ds.value_counts().index[0])"""





def item_21():
    ds=pd.Series(np.random.randint(1,10,10))
    print(ds)
    print([i for i in ds if i%5==0])


def item_22():
    num_series = pd.Series(list('2390238923902390239023'))
    element_get=[0,2,6,11,21]
    result=num_series.take(element_get) #cool method
    print(result)


def item_23():
    ds1=pd.Series([1,2,3,4,5,6,7,8,9,11])
    ds2=pd.Series([1,3,5,7,10])
    

    #Him solution
    #result=ds1[ds1.isin(ds2)]
    #print(list(result.index))

    #W3 solution
    #print(pd.Index(ds1).get_loc(1))


def item_24():
    ds=pd.Series(['php','python','java','c#'])
    #W3 school
    #result=ds.map(lambda x:x[0].upper()+x[1:-1]+x[-1].upper())
    #print(result)

    #Him solution
    ds=pd.Series([i[0].upper()+i[1:-1]+i[-1].upper() for i in ds])
    print(ds)


def item_25():
    ds=pd.Series(['php','python','java','c#'])
    #Him solution 1
    result1=ds.map(lambda x:len(x))
    print(result1)


    #Him solution 2
    result2=pd.Series([len(i) for i in ds])
    print(result2)


def item_26():
    ds=pd.Series([1,3,5,8,10,11,15])
    #W3 solution Method
    print(ds.diff())

    #Him solution
    for i in range(len(ds)-1,-1,-1):
        if i==0:
            ds[i]=None
            continue
        ds[i]=ds[i]-ds[i-1]

    print(ds)


def item_27():
    date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
    print(pd.to_datetime(date_series))


def item_28():
    from dateutil.parser import parse
    date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
    date_series_2=date_series
    print(date_series)
    date_series=date_series.map(lambda x:parse(x))
    print(date_series)
    date_series_2=pd.to_datetime(date_series_2)
    print(date_series_2)
    print(date_series.dt.day.tolist())
    print(date_series.dt.dayofyear.tolist())
    print(date_series.dt.isocalendar())
    #print(date_series.dt.weekday_name.tolist())


def item_29():
    date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
    date_series=date_series.map(lambda x:'10'+x)
    date_series=pd.to_datetime(date_series)
    print(date_series)


def item_30():
    from collections import Counter
    color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
    #color_series=color_series.map(lambda x:)
    check_map=color_series.map(lambda x: len([i for i in x if i.lower() in 'aeiou'])>=2)
    print(color_series[check_map])


def item_31():
    ds1=pd.Series([1,2,3,4,5,6,7,8,9,10])
    ds2=pd.Series([11,8,7,5,6,5,3,4,7,1])

    print((sum((ds1-ds2)**2))**(1/2))


def item_32():
    nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
    both_sides_position=[i for i in range(1,len(nums)-1) if nums[i-1]<nums[i]>nums[i+1]]
    print(both_sides_position)


def item_33():
    str1 = 'abc def abcdef icd'
    ds1=pd.Series(list(str1))
    print(ds1)
    ds1=ds1.replace(' ',ds1.value_counts().index.tolist()[-1])
    print(''.join(ds1))


def item_34():
    #งง
    pass


def item_35():
    ds1=pd.Series(pd.date_range('2020-01-01',periods=52,freq='W-SUN'))  #จำ
    #=pd.Series([i for i in ds1.day_name() if i=='Sunday'])
    print(ds1)
    #Common solution
    ds2=pd.date_range('2020-01-01',periods=52,freq='W')
    #print(ds2)
    sunday_series=pd.Series([i for i in ds2 if i.day_name()=='Sunday'])
    print(sunday_series)



def item_36():
    ds1=pd.Series(list('ABCDEFGHIJKLMNOP'))
    df=pd.DataFrame(zip(ds1,list(ds1.index)))
    print(df)

def item_37():
    series1 = pd.Series(range(10))
    series2 = pd.Series(list('pqrstuvwxy'))
    print(series2.append(series1)) #Stack verical
    print(pd.DataFrame(zip(series1,series2)))


def item_38():
    nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
    nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
    print(nums1==nums2)

def item_39():
    nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])

    #Method solution
    print(nums.idxmax())
    print(nums.idxmin())


    #Common solution incase forget method
    print(nums[nums == max(nums)].index[0]) # 1
    print([i for i in range(len(nums)) if nums[i]==max(nums)][0]) #Super common


def item_40():
    df_data = pd.DataFrame({'W': [68, 75, 86, 80, None], 'X': [78, 75, None, 80, 86], 'Y': [84, 94, 89, 86, 86],
                            'Z': [86, 97, 96, 72, 83]})
    sr_data = pd.Series([68, 75, 86, 80, None])

    #Method solution
    print(df_data.ne(sr_data,axis=0))


    #common method
    result=(pd.DataFrame([sr_data!=df_data[i] for i in df_data],index=[j for j in df_data])).transpose()
    print(result)

item_40()














