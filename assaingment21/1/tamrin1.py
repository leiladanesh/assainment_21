import  cv2
import numpy as np
flag=True
sq=np.zeros((400,400),dtype='uint8')
row,col= sq.shape
m=sq.shape[0]//8
n=sq.shape[1]//8
for i in range(0,sq.shape[0],m):
    for j in range(0,sq.shape[1],n):
        if  flag ==False :
            sq[i:i+m,j:j+n]=255
            flag=True
        else:
            sq[i:i+m ,j:j+n] = 0
            flag= False
    if flag:
        flag=False
    else:
        flag =True
cv2.imshow('ss',sq)
cv2.waitKey()