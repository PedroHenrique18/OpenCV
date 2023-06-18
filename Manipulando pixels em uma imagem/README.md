# 2.2. Exercícios

-Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa regions.py. Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1
 e P2
 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1
 e P2
 será exibida com o negativo da imagem na região correspondente.
 
 # Regions.py
```
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
```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Manipulando%20pixels%20em%20uma%20imagem/regions.png">
</div>


-Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa trocaregioes.py. Seu programa deverá trocar os quadrantes em diagonal na imagem. Explore o uso da classe Mat e seus construtores para criar as regiões que serão trocadas.

# trocaregioes.py
```
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
```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Manipulando%20pixels%20em%20uma%20imagem/trocaregioes.png">
</div>

 
 

<div align="center">
  <small>Pedro Henrique Bezerra Fernandes - 2023</small>
</div>
