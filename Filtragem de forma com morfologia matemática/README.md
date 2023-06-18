# 13.2.  Exercícios

◉Usando o programa morfologia.cpp como referência, crie um programa que resolva o problema da pré-filtragem de forma para reconhecimento dos caracteres usando operações morfológicas. Você poderá usar as imagens digitos-1.png, digitos-2.png, digitos-3.png, digitos-4.png e digitos-5.png para testar seu programa. Cuidado para deixar o ponto decimal separado dos demais dígitos para evitar um reconhecimento errado do número no visor.
 
 # [morfologia.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20de%20forma%20com%20morfologia%20matem%C3%A1tica/morfologia.py)
```
import cv2
import numpy as np

def prefiltragem(imagem):
    # Elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Erosão
    erosao = cv2.erode(imagem, elemento_estruturante)

    # Dilatação
    dilatacao = cv2.dilate(imagem, elemento_estruturante)

    # Abertura
    abertura = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, elemento_estruturante)

    # Fechamento
    fechamento = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, elemento_estruturante)

    # Abertura seguida de fechamento
    abertfecha = cv2.morphologyEx(abertura, cv2.MORPH_CLOSE, elemento_estruturante)

    # Concatenar as imagens em uma única linha
    imagens = np.hstack((erosao, dilatacao, abertura, fechamento, abertfecha))

    return imagens

# Carregar as imagens de teste
imagens_teste = ['digitos-1.png', 'digitos-2.png', 'digitos-3.png', 'digitos-4.png', 'digitos-5.png']

for imagem_teste in imagens_teste:
    # Carregar a imagem
    imagem = cv2.imread(imagem_teste, cv2.IMREAD_GRAYSCALE)

    if imagem is None:
        print(f"Erro ao carregar a imagem: {imagem_teste}")
        continue

    # Realizar a pré-filtragem
    imagem_filtrada = prefiltragem(imagem)

    # Exibir a imagem original e a imagem pré-filtrada
    cv2.imshow("Imagem Original", imagem)
    cv2.imshow("Imagem Pré-filtrada", imagem_filtrada)

    cv2.waitKey(0)

cv2.destroyAllWindows()
```

•Digitos fornecidos 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20de%20forma%20com%20morfologia%20matem%C3%A1tica/digitos%20fornecidos.png">
</div>

•Digito 1 filtrado 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20de%20forma%20com%20morfologia%20matem%C3%A1tica/digito%201.png">
</div>

•Digito 2 filtrado 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20de%20forma%20com%20morfologia%20matem%C3%A1tica/digito%202.png">
</div>

•Digito 3 filtrado 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20de%20forma%20com%20morfologia%20matem%C3%A1tica/digito%203.png">
</div>

•Digito 4 filtrado 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20de%20forma%20com%20morfologia%20matem%C3%A1tica/digito%204.png">
</div>

•Digito 5 filtrado 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20de%20forma%20com%20morfologia%20matem%C3%A1tica/digito%205.png">
</div>


