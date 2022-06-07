import numpy as np
np.random.seed(1)
import tensorflow as tf
import keras
train_X = np.array([[0,0],[0,1],[1,0],[1,1]])
train_y = np.array([0,1,1,0]) 
#We create a Sequential model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, input_dim=2, activation='sigmoid')) # Hidden Layer
model.add(tf.keras.layers.Dense(1, input_dim=2, activation='sigmoid')) # Output Layer
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.SGD(lr=1.0), metrics=['accuracy'])
model.fit(train_X, train_y, epochs= 5000)



W=model.get_weights()

keras.utils.plot_model(model)

import numpy as np 
X=np.arange(0,1,0.05)
Y=np.arange(0,1,0.05)
X,Y=np.meshgrid(X,Y)
ans=np.array([X,Y])
all_points=[list(ans[:,i,j]) for i in range(20) for j in range(20)]

z=model.predict(all_points).reshape(20,20)

z.shape,X.shape,Y.shape

%matplotlib inline

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_wireframe(X,Y,z)
X2D=np.arange(0,1,0.1)
for i in range(2):
  Y2D=-W[0][0][i]*X2D/W[0][1][i]-W[1][i]/W[0][1][i]
  plt.plot(X2D,Y2D)
ax.view_init(30, 10)
plt.draw()


W
W[0][:,1]

W[1][0]

W[0][0][0],W[0][1][0]

X2D=np.arange(0,1,0.1)
Y2D=-W[0][0][0]*X2D/W[0][1][0]-W[1][0]/W[0][1][0]
plt.plot(X2D,Y2D)
Y2D=-W[0][0][1]*X2D/W[0][1][1]-W[1][0]/W[0][1][1]
plt.plot(X2D,Y2D)
plt.show()