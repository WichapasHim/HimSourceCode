# Import package
import pandas as pd
import datetime as dt
#print(dt.date(2019,1,1))

# Raw Data
CostItem = {
    'ID':[1, 2, 3, 4, 5],
    'Name':['Cost A', 'Cost B', 'Cost C', 'Cost D', 'Cost E'],
    'IsActive':['True', 'True', 'True', 'False', 'True']}

CostItemPrice = {
    'ID':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'CostItemID': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5],
    'Price': [100, 110, 120, 130, 50, 60, 70, 10, 20, 200, 100],
    'EffectiveDate': [dt.datetime(2019,1,1), dt.datetime(2019,7,1), dt.datetime(2020,1,1), dt.datetime(2020,7,1), dt.datetime(2019,1,1), dt.datetime(2019,7,1), dt.datetime(2020,1,1), dt.datetime(2019,1,1), dt.datetime(2019,7,1), dt.datetime(2019,1,1), dt.datetime(2019,1,1)],
    'IsActive':[True, False, True, True, True, True, True, True, True, True, False]}

Project = {
    'ID':[1, 2, 3],
    'Name':['Project A', 'Project B', 'Project C'],
    'StartDate':[dt.datetime(2019,2,1), dt.datetime(2019,8,1), dt.datetime(2020,3,1)]}

# Convert into DataFrame
dfCostItem = pd.DataFrame(CostItem)
dfCostItemPrice = pd.DataFrame(CostItemPrice)
dfProject= pd.DataFrame(Project)


# Filter IsActive == 'True'
dfCostItem = dfCostItem[dfCostItem['IsActive'] == 'True']
dfCostItemPrice = dfCostItemPrice[(dfCostItemPrice['CostItemID'].isin(dfCostItem['ID'])) & (dfCostItemPrice['IsActive'] == True)]


# Find Result

dfresult_2 = pd.merge(dfProject,dfCostItemPrice, how = 'cross')
dfresult = dfresult_2[dfresult_2['StartDate'] > dfresult_2['EffectiveDate']]
dfresult = dfresult.copy()

dfresult['IsActive'] = dfresult.groupby(['ID_x', 'CostItemID'])['EffectiveDate'].rank(ascending = 0)

dfMaxDate = dfresult[dfresult['IsActive'] == 1]
#dfMaxDate=dfMaxDate.rename(columns={'Price': 'TotalCost','ID_x: 'ID'})

dfFinale = dfMaxDate.groupby(['ID_x', 'Name', 'StartDate']).agg({'Price':'sum'})

#dfFinale = dfFinale.rename(columns = {'Price': 'TotalCost','ID_x': 'ID'})


#print(dfresult)
#print(dfFinale)

