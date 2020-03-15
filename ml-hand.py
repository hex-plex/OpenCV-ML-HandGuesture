import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

lis=['up','down','right','left']
model1=keras.Sequential([
	keras.layers.Conv2D(200,(3,3),activation='tanh',input_shape=(200,200,3)),
	keras.layers.AveragePooling2D((2,2),padding='valid' ),
	keras.layers.Conv2D(300,(5,5),activation='relu'),
	keras.layers.AveragePooling2D((2,2),padding='valid'),
	keras.layers.Flatten(),
	keras.layers.Dense(1,activation='softmax')
	])
model1.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model2=keras.Sequential([
	keras.layers.Conv2D(200,(3,3),activation='tanh',input_shape=(200,200,3)),
	keras.layers.AveragePooling2D((2,2),padding='valid' ),
	keras.layers.Conv2D(300,(5,5),activation='relu'),
	keras.layers.AveragePooling2D((2,2),padding='valid'),
	keras.layers.Flatten(),
	keras.layers.Dense(1,activation='softmax')
	])
model2.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model3=keras.Sequential([
	keras.layers.Conv2D(200,(3,3),activation='tanh',input_shape=(200,200,3)),
	keras.layers.AveragePooling2D((2,2),padding='valid' ),
	keras.layers.Conv2D(300,(5,5),activation='relu'),
	keras.layers.AveragePooling2D((2,2),padding='valid'),
	keras.layers.Flatten(),
	keras.layers.Dense(1,activation='softmax')
	])
model3.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model4=keras.Sequential([
	keras.layers.Conv2D(200,(3,3),activation='tanh',input_shape=(200,200,3)),
	keras.layers.AveragePooling2D((2,2),padding='valid' ),
	keras.layers.Conv2D(300,(5,5),activation='relu'),
	keras.layers.AveragePooling2D((2,2),padding='valid'),
	keras.layers.Flatten(),
	keras.layers.Dense(1,activation='softmax')
	])
model4.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

pred=[1]*200+[2]*200+[3]*200+[4]*200
pred=np.array(pred)

models=[model1,model2,model3,model4]
