import pandas as pd
import csv

df=pd.read_csv("agoda.csv")
total_customer=len(df.columns)
print(total_customer)