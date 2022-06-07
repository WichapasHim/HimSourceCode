import pandas as pd
import datetime as dt
item={
    'item_id':[1,2,3,4,5,6],
    'item_name':["""7” MATERIAL-A""","""12” MATERIAL-A""","""9” MATERIAL-B""","""20” MATERIAL-B""",'MATERIAL-C','MATERIAL-D'],
    'is_active':[1,1,1,0,1,1]
}

item_price={
    'item_price_id':[1,2,3,4,5,6,7,8,9,10,11,12,13],
    'item_id':[1,1,1,1,2,2,2,3,3,4,5,5,6],
    'price':[100,120,140,160,60,80,100,10,20,200,100,200,300],
    'effective_date':[dt.date(2020,1,1),dt.date(2020,7,1),dt.date(2021,1,1),dt.date(2021,7,1),dt.date(2020,1,1),dt.date(2020,7,1),dt.date(2021,1,1),dt.date(2020,1,1),dt.date(2020,7,1),dt.date(2020,1,1),dt.date(2020,1,1),dt.date(2021,1,1),dt.date(2021,1,1)],
    'is_active':[1,0,1,1,1,1,1,1,1,1,0,0,1]
}


project={
    'project_id':[1,2,3],
    'project_name':['Project A','Project B','Project C'],
    'project_start':[dt.date(2020,2,1),dt.date(2020,8,1),dt.date(2021,3,1)]
}


df_item=pd.DataFrame(item)
df_item_price=pd.DataFrame(item_price)
df_project=pd.DataFrame(project)

df_item_active=df_item[df_item['is_active']==1]
df_item_price_active=df_item_price[df_item_price['is_active']==1]
df_item_price_active=df_item_price_active[df_item_price_active['effective_date']<max(df_project['project_start'])]

df_combine_1=pd.merge(df_item_active,df_item_price_active,on='item_id',how='outer')
df_combine_1=df_combine_1.dropna()
df_combine_2=df_project.merge(df_combine_1,how='cross')
df_combine_2=df_combine_2[df_combine_2['project_start']>df_combine_2['effective_date']]
df_A=df_combine_2[df_combine_2['project_name']=='Project A']
df_B=df_combine_2[df_combine_2['project_name']=='Project B']
df_B_1=df_B[(df_B['effective_date']<df_B['project_start'])&(df_B['effective_date']>min(df_B['effective_date']))]
df_B_2=df_B[df_B['item_name']=='7” MATERIAL-A']
df_B=df_B_1.merge(df_B_2,how='outer')
df_C=df_combine_2[df_combine_2['project_name']=='Project C']
df_C_1=df_C[(df_C['effective_date']<df_C['project_start'])&(df_C['effective_date']>min(df_C['effective_date']))]
df_C_1.drop(19,inplace=True)
df_result=df_A.merge(df_B,how='outer')
df_result=df_result.merge(df_C_1,how='outer')
df_result.drop(['is_active_x','is_active_y'],axis='columns',inplace=True)
print(df_result)

                  
    





