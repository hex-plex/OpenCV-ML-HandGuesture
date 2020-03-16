import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np
import  vlc
import subprocess as sp

#player=vlc.MediaPlayer("/home/hexplex0xff/Downloads/videoplayback.mp4")
model=keras.models.load_model("model.h5")
cam=cv2.VideoCapture(0)
frame=cam.read()[1]
cv2.waitKey(1)
r=cv2.selectROI(frame)
prev=-1
while True:
    m=cam.read()[1]
    cv2.rectangle(m,tuple([int(r[0]+r[2]/2-100),int(r[1]+r[3]/2-100)]),tuple([int(r[0]+r[2]/2+100),int(r[1]+r[3]/2+100)]),(0,255,0),3)
    cv2.imshow('frame',m)
    m1=m[int(r[1]+r[3]/2-100):int(r[1]+r[3]/2+100),int(r[0]+r[2]/2-100):int(r[0]+r[2]/2+100),:]
    cv2.imshow('cutout',m1)
    m1=cv2.resize(m1,(100,100))
    m1=m1.reshape((1,)+m1.shape)
    pred=model.predict(m1)
    a=max(pred)
    #print(pred)
    if a.all()>=0.6:
        i=np.argmax(pred)
        if i==0 and prev!=0:
            sp.Popen(['vlc-ctrl','volume','+10%'])
            print('up')
            #Process1
        elif i==1 and prev!=1:
            sp.Popen(['vlc-ctrl','volume','-10%'])
            print('down')
            #process2
        elif i==2 and prev!=2:
            i=2
            print('right')
            #player.play()
            #process3
        elif i==3 and prev!=3:
            i=3
            print('left')
            #player.pause()
            #process4
        prev=i

    if cv2.waitKey(1) & ord('q')==0xFF:
        break
cam.release()
