import cv2 as cv
import numpy as np

img = cv.imread('Pedro2.jpg')

#mostrar so a imagem
cv.imshow('pedro',img)

# 1. Pinte a imagem com uma determinada cor
img[200:300, 300:400] = 0,0,255
cv.imshow('Green', img)

# 2. Desenhe um retângulo
cv.rectangle(img, (0,0), (img.shape[1]//2, img.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', img)

# 3. Desenhando um circulo
cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', img)

# 4. Desenhe uma linha
cv.line(img, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', img)

# 5. escrever um texto
cv.putText(img, 'Hello, my name is Pedro!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', img)

cv.waitKey(0)