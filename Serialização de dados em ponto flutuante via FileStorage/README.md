# 3.2. Exercícios

◉Utilizando o programa filestorage.cpp como base, crie um programa [filestorage.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Serializa%C3%A7%C3%A3o%20de%20dados%20em%20ponto%20flutuante%20via%20FileStorage/filestorage.py) que gere uma imagem de dimensões 256x256 pixels contendo uma senóide de 4 períodos com amplitude de 127 desenhada na horizontal, como aquela apresentada na Figura 6 . Grave a imagem no formato PNG e no formato YML. Compare os arquivos gerados, extraindo uma linha de cada imagem gravada e comparando a diferença entre elas. Trace um gráfico da diferença calculada ao longo da linha correspondente extraída nas imagens. O que você observa?
 
 # filestorage.py
```
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
```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Serializa%C3%A7%C3%A3o%20de%20dados%20em%20ponto%20flutuante%20via%20FileStorage/filestorage.png">
</div>
