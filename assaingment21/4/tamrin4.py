import cv2

img = cv2.imread('4.jpg', 0)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j] < 150:
            img[i, j] = 0
            
cv2.imshow('wolf', img)
cv2.waitKey()