import cv2 as cv
import numpy as np

img = cv.imread('pedro.jpg')

altura, largura = img.shape[:2] 

x1=int(input("valor entre 0 e %d de x1 "% (altura)))
y1=int(input("valor entre 0 e %d de y1 "% (largura)))
x2=int(input("valor entre 0 e %d de x2 "% (altura)))
y2=int(input("valor entre 0 e %d de y2 "% (largura)))

for i in range(x1, x2): #percorre linhas
 for j in range(y1, y2): #percorre colunas
  pixel = img[i,j]

  pixel[0] = 255 - pixel[0]
  pixel[1] = 255 - pixel[1]
  pixel[2] = 255 - pixel[2]

  pixel = img
  

# Convertendo para negativo
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', 255-gray)
cv.imshow("Imagem modificada", img)
cv.waitKey(0)