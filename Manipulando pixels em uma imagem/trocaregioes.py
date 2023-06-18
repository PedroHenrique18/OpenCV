import cv2 as cv
import numpy as np

img = cv.imread('pedro.jpg')
img2 = cv.imread('pedro.jpg')

altura, largura = img.shape[:2] 

x= int(altura-(altura/2))
y =int( largura -(largura/2))
print(x,y)

for i in range(0, x): #percorre linhas
 for j in range(0, y): #percorre colunas
  img2[i,j]=img[i+x,j+y]
  img2[i+x,j]=img[i,j+y]
  img2[i,j+y]=img[i+x,j]
  img2[i+x,j+y]=img[i,j]
  
   

cv.imshow("Imagem modificada", img2)
cv.imshow("img", img)
cv.waitKey(0)