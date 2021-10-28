import numpy as np 
import matplotlib.pyplot as plt

x=np.arange(0.00001,1.01,0.01)
y=-x*np.log2(x)-(1-x)*np.log2(1-x)
y1=(1-x**2-(1-x)**2)*2
plt.plot(x,y,'b')
plt.plot(x,y1,'g')

import pandas as pd
df=pd.read_csv('Iris.csv')
df.head()

df.Species.value_counts()

from sklearn import tree
X = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
Y = df['Species']
clf = tree.DecisionTreeClassifier(min_samples_leaf=5,min_impurity_decrease=0.1,criterion="entropy")
clf = clf.fit(X, Y)

clf.predict(X[46:56])

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None, 
                      feature_names=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'],  
                      class_names=df['Species'].unique(),  
                      filled=True, rounded=True,  
                      special_characters=True)  
graph = graphviz.Source(dot_data) 
graph