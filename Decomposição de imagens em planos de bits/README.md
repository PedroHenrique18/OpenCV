# 2.2. Exercícios

◉Usando o programa esteg-encode.cpp como referência para esteganografia, escreva um programa [esteg-encode.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Decomposi%C3%A7%C3%A3o%20de%20imagens%20em%20planos%20de%20bits/esteg_encode.py) que recupere a imagem codificada de uma imagem resultante de esteganografia. Lembre-se que os bits menos significativos dos pixels da imagem fornecida deverão compor os bits mais significativos dos pixels da imagem recuperada. O programa deve receber como parâmetros de linha de comando o nome da imagem resultante da esteganografia
 
 # esteg-encode.py
```
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
```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Decomposi%C3%A7%C3%A3o%20de%20imagens%20em%20planos%20de%20bits/esteg_encode.png">
</div>

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Decomposi%C3%A7%C3%A3o%20de%20imagens%20em%20planos%20de%20bits/esteg_encode_2.png">
</div>

