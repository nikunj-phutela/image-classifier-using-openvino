import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation,Flatten,Conv2D,MaxPooling2D
import pickle
from tensorflow.keras.callbacks import TensorBoard
import time
from keras.utils import to_categorical


X_train=pickle.load(open("X1_train.pickle","rb"))
Y_train=pickle.load(open("Y1_train.pickle","rb"))
X_test=pickle.load(open("X1_test.pickle","rb"))
Y_test=pickle.load(open("Y1_test.pickle","rb"))



y_train = to_categorical(Y_train)
y_test = to_categorical(Y_test,46)


model=Sequential()

#first layer

model.add(Conv2D(64,(3,3),input_shape=X_train.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#second layer

model.add(Conv2D(128,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#third layer

model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))

#output layer

model.add(Dense(46))
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

model.fit(X_train,y_train,epochs=10,validation_data=(X_test,y_test))

model.save('DL-DWI-100x100-CNN-46-4-val')
