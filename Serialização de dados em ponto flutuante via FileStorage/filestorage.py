import cv2 as cv
import numpy as np
import math

side = 256
periodos = 4

#criando matriz 
img = np.zeros((side,side), dtype='float32')

for i in range(0, side):
    for j in range(0, side):
      img[j, i] =float( 127 * math.sin(2 *3.14 * periodos * j / side) + 128)
    
cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
# Converte a imagem de origem em array Numpy inteiro de 8 bits sem sinal
arr = np.uint8(img)

cv.imshow("image", arr)
cv.waitKey()






