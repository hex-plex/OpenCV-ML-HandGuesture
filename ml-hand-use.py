import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np

model=keras.models.load_model("model.h5")
cam=cv2.VideoCapture(0)
frame=cam.read()[1]
cv2.waitKey(1)
r=cv2.selectROI(frame)
while True:
    m=cam.read()[1]
    cv2.rectangle(m,tuple([int(r[0]+r[2]/2-100),int(r[1]+r[3]/2-100)]),tuple([int(r[0]+r[2]/2+100),int(r[1]+r[3]/2+100)]),(0,255,0),3)
    cv2.imshow('frame',m)
    m1=m[int(r[1]+r[3]/2-100):int(r[1]+r[3]/2+100),int(r[0]+r[2]/2-100):int(r[0]+r[2]/2+100),:]
    cv2.imshow('cutout',m1)
    m1=cv2.resize(m1,(100,100))
    m1=m1.reshape((1,)+m1.shape)
    pred=model.predict(m1)
    print(pred)
    if cv2.waitKey(1) & ord('q')==0xFF:
        break
cam.release()
