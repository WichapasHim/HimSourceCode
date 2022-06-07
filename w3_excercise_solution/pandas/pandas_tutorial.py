import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#intro
def item_1():
    my_date_set={
        'car' : ['BMW','TOYOTA','HONDA'],
        'passing':[3,7,2]
    }
    
    my_var=pd.DataFrame(my_date_set)
    print(my_var)
    print(my_var['car'][0])
    

 




#Series
def item_2():
    a=[1,7,2]
    my_var=pd.Series(a)
    print(my_var)
    print(my_var[1])
    

def item_3():
    a=[1,7,2]
    my_var=pd.Series(a,index=['x','y','z'])
    print(my_var)
    print(my_var['x'])
    print(my_var[0])
    
    
def item_4():
    cal={'day1':420,'day2':380,'day3':390}

    my_var=pd.Series(cal)
    print(my_var)
    print(my_var['day1'])
    print(my_var[0])
    
    
def item_5():
    cal={'day1':420,'day2':380,'day3':390}
    
    my_var=pd.Series(cal,index=(list(cal.keys()))[:2])
    print(my_var)



#DataFrames
def item_6():
    data = {
            "calories": [420, 380, 390,200,300],
            "duration": [50, 40, 45,10,20]
            }


    df=pd.DataFrame(data)
    
    print(df)
    #print(type(df.loc[0]))
    #print(df.loc[list(range(3))])




def item_7():
    data = {
            "calories": [420, 380, 390,200,300],
            "duration": [50, 40, 45,10,20]
            }


    df=pd.DataFrame(data,index=['day1','day2','day3','day4','day5'])    
    print(df)
    print(df.loc[['day1','day2']])


#Read Csv
def item_8():
    
    df=pd.read_csv('data.csv')
    
    print(df.to_string())#  to_string method is used to print all row




#Read JSON
def item_9():
    
    df=pd.read_json('data.json')
    
    print(type(df['Duration'][0]))


#Analyzed data
def item_10():
    df=pd.read_csv('data.csv')
    print(df.head())
    print(df.tail(10))
    print(df.info())
    
    
#Cleaning data
def item_11():
    df=pd.read_csv('dirty_data.csv')
    
    
    #Dropทิ้งแม่้ง
    #df=df.dropna()
    #df.dropna(inplace=True)
    
    
    #Fill empty with values
    #df=df.fillna('BET')
    #df.fillna('BET',inplace=True)
    #df['Calories']=df['Calories'].fillna('BET')
    #df['Calories'].fillna('BET',inplace=True)
    
    
    #Fill with statistics values -> Mean Mode Median
    
    df['Calories'].fillna(df['Calories'].mean(),inplace=True)
    
    print(df)
    print(type(df['Calories'].mode()))
    
    


#Wrong format
def item_12():
    df=pd.read_csv('dirty_data.csv')
    #print(df)
    df['Date']=pd.to_datetime(df['Date'])
    #print(type(pd.to_datetime(df['Date'])))
 
    #print(df)
    #df.loc[7,'Duration']='BET'  #Can be used if data is not so big
    #print(df.loc[7,'Duration'])
    #print(df.index)
    
    
    #Big data using loop to replace val
""" for i in df.index:
        if df.loc[i,'Duration']>120:
            df.loc[i,'Duration']=100
    print(df)
    
    
    for i in df.index:
        if df.loc[i,'Duration']>90:
            df.drop(i,inplace=True)
            
    print(df)"""
    
    
    
    
    
    
#Duplicate
def item_13():
    df=pd.read_csv('dirty_data.csv')
    print(df.duplicated())
    print(type(df.duplicated()))
    df.drop_duplicates(inplace=True)
    print(df.duplicated())
    
    
def item_14():
    df=pd.read_csv('data.csv')
    #print(df.corr())
    
    
    
    #df.plot()
    #plt.show()
    
    df.plot(kind='scatter',x='Duration',y='Calories')
    plt.show()
    


def item_15():
    df=pd.read_csv('data.csv')
    print(df)
    print(df.iloc[1])
    
    



#W3resource
def item_16():
    s=pd.Series([1,4,np.nan,8])
    #print(s)
    dates=pd.date_range('20190101',periods=8)
    print(type(dates))
    df=pd.DataFrame(np.random.rand(8,4),index=dates,columns=list('ABCD'))
    print(df)
    
item_16()