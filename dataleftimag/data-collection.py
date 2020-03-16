import  cv2
import time
cam=cv2.VideoCapture(0)
i=0
frame=cam.read()[1]
cv2.imshow('frame',frame)
roi=cv2.selectROI(frame)
cv2.waitKey(1)
time.sleep(1)
while i<500:
    frame=cam.read()[1]
    cv2.imwrite('dataleft'+str(i)+'.jpg',frame[int(roi[1]+(roi[3]/2)-100):int(roi[1]+(roi[3]/2)+100),int(roi[0]+roi[2]/2-100):int(roi[0]+roi[2]/2+100)])
    cv2.imshow('fram',frame[int(roi[1]+(roi[3]/2)-100):int(roi[1]+(roi[3]/2)+100),int(roi[0]+roi[2]/2-100):int(roi[0]+roi[2]/2+100)])
    i+=1
    if cv2.waitKey(2) and ord('q')==0xFF:
	break
cam.release()
