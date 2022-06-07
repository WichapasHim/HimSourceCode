import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

sum_df=df.groupby('Country/Region').sum()

sum_df=sum_df.reset_index()

time_series_df=sum_df.set_index('Country/Region').T[2:]

time_series_df['Thailand'].plot()
time_series_df['Burma'].plot()


#Sigmoid function

import numpy as np

x=np.arange(-10,10,0.1)
y=1/(1+np.exp(-x))

import matplotlib.pyplot as plt

m=40000
alpha=0.5
d=3
y=1/(1+np.exp(-x))*m
y1=1/(1+np.exp(-alpha*x))*m
y2=1/(1+np.exp(-alpha*(x-d)))*m
plt.plot(x,y)
plt.plot(x,y1)
plt.plot(x,y2)

x=np.array([20,21,22,23,24])
y=np.array([50,55,62,68,80])
plt.plot(x,y,'r.')

def func(x,m,alpha,d):
      return m/(1+np.exp(-alpha*(x-d)))

y=list(time_series_df['Burma'])[210:]
x=[i for i in range(len(y))]
plt.plot(x,y,'r+')


from scipy.optimize import curve_fit 

t,v = curve_fit(func,x,y,bounds=([40000,0,0],[200000,0.4,200]))


x1 = [i for i in range(400)]
y_predicted = func(x1,t[0],t[1],t[2])
plt.plot(x,y,'r+')
plt.plot(x1,y_predicted)
plt.show()
t