from sklearn.cluster import KMeans
import numpy as np

X=np.array([[1,1],[1,2],[2,1],[4,3],[4,4],[5,3]])
km=KMeans(n_clusters=2).fit(X)
km.cluster_centers_

import matplotlib.pyplot as plt
plt.plot(X.T[:][0],X.T[:][1],'g.')
plt.plot(km.cluster_centers_.T[:][0],km.cluster_centers_.T[:][1],'r+')

import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
df.columns=['sepal length','sepal width','petal length','petal width','class']
X=df[['sepal length','sepal width','petal length','petal width']]
km=KMeans(n_clusters=2).fit(X)
km.cluster_centers_


q=[]
for k in range(2,11):
  km=KMeans(n_clusters=k).fit(X)
  q.append(km.inertia_)
plt.plot([i for i in range(2,11)],q)

q=[]
for k in range(2,11):
  km=KMeans(n_clusters=k).fit(X)
  q.append(km.inertia_)
plt.plot([i for i in range(2,11)],q)

import seaborn as sb
chart=sb.scatterplot(df['petal length'],df['petal width'],hue=df['class'])
chart.plot(km.cluster_centers_.T[:][2:3],km.cluster_centers_.T[:][3:4],'r+')