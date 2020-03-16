import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import gc
lis=['up','down','right','left']
model=keras.Sequential([
	keras.layers.Conv2D(50,kernel_size=3,activation='tanh',input_shape=(100,100,3)),
	keras.layers.AveragePooling2D((2,2),padding='valid' ),
	keras.layers.Conv2D(100,kernel_size=3,activation='relu'),
	keras.layers.AveragePooling2D((2,2),padding='valid'),
	keras.layers.Flatten(),
	keras.layers.Dense(4,activation='softmax')
	])
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

pred=[[1,0,0,0]]*500+[[0,1,0,0]]*500+[[0,0,1,0]]*500+[[0,0,0,1]]*500
pred=np.array(pred)


X=[]

for i in range(4):
	print("*"*10+str(i+1)+"*"*10)
	X=[]
	print(pred[500*i:500*i+500])
	for j in range(500):
		gc.collect()
		print(j+1)
		temp=cv2.imread("/home/hexplex0xff/Desktop/hand gesture/data"+lis[i]+"imag/data"+lis[i]+str(j)+".jpg")
		temp=cv2.resize(temp,(100,100))
		cv2.imshow('frame',temp)
		cv2.waitKey(1)
		X.append(temp)
	X=np.array(X)
	model.fit(X,pred[500*i:500*i+500],epochs=50)
model.save("model.h5")
print("done Model ")
