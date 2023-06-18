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
