import vcr2
import cv2
import time
import numpy as np
fourcc=vcr2.VideoWriter_fourcc(*"XVID")
output_file=vcr2.VideoWriter("output.avi",fourcc,20.0,(640,480))
cap=vcr2.VideoCapture(0)
time.sleep(2)
bg=0
for i in range(60):
    ret,bg=cap.read()

bg=np.flip(bg,axis=1)
while(cap.isOpened()):
    ret_img=cap.read()
    if not ret:
        break

    img=np.flip(img,axis=1)
    hsv=vcr2.cvtColor(img,vcr2.COLOR_BGR2HSV)
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask_1=vcr2.inRange(hsv,lower_red,upper_red)

    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask_2=vcr2.inRange(hsv,lower_red,upper_red)

    mask_1=mask_1+mask_2

    mask_1=vcr2.morphologyEx(mask_1,vcr2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_1=vcr2.morphologyEx(mask_1,vcr2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask_2=vcr2.bitwise_not(mask_1)
    res_1=vcr2.bitwise_and(img,img,mask=mask_2)
    res_2=vcr2.bitwise_and(bg,bg,mask=mask_1)
    final_output=vcr2.addWeighted(res_1,1,res_2,1,0)
    vcr2.imshow("magic",final_output)
    vcr2.waitKey(1)
cap.release()
out.release()
vcr2.destroyAllWindows()