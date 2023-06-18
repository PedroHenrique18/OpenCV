import cv2 as cv
import numpy as np
import random

img = cv.imread('sushi.png')
altura, largura = img.shape[:2] 
img1 = np.zeros((altura, largura, 3 ), np.uint8)
img2 = np.zeros((altura, largura, 3 ), np.uint8)

for i in range(altura):
    for j in range(largura):
        for k in range(3):
            v1 = format(img[i][j][k], '08b')
            v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
            v3 = v1[4:] + chr(random.randint(0, 1)+48) * 5

            img1[i][j][k]= int(v2, 2)
            img2[i][j][k]= int(v3, 2)

cv.imshow("image1", img1)
cv.imshow("image2", img2)

cv.waitKey(0)