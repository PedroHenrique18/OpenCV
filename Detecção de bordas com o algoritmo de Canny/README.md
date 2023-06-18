# 11.3. Exercícios

◉Utilizando os programas exemplos/canny.cpp e exemplos/pontilhismo.cpp como referência, implemente um programa cannypoints.cpp. A idéia é usar as bordas produzidas pelo algoritmo de Canny para melhorar a qualidade da imagem pontilhista gerada. A forma como a informação de borda será usada é livre. Entretanto, são apresentadas algumas sugestões de técnicas que poderiam ser utilizadas:

Desenhar pontos grandes na imagem pontilhista básica;

Usar a posição dos pixels de borda encontrados pelo algoritmo de Canny para desenhar pontos nos respectivos locais na imagem gerada.

Experimente ir aumentando os limiares do algoritmo de Canny e, para cada novo par de limiares, desenhar círculos cada vez menores nas posições encontradas.
 
 # [cannypoints.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Detec%C3%A7%C3%A3o%20de%20bordas%20com%20o%20algoritmo%20de%20Canny/cannypoints.py)
```
import cv2
import sys
import numpy as np

def generate_dotted_image(image, border):
    dotted_image = np.copy(image)
    height, width = image.shape[:2]

    # Obter as coordenadas dos pixels de borda
    edge_coords = np.nonzero(border)

    # Desenhar pontos menores na imagem pontilhista básica
    for x, y in zip(edge_coords[0], edge_coords[1]):
        cv2.circle(dotted_image, (y, x), 2, (0, 0, 0), -1)

    return dotted_image

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Informe o caminho para a imagem de entrada.")
        exit()

    image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Erro ao abrir a imagem.", sys.argv[1])
        exit()

    # Converter a imagem em escala de cinza para colorida
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Aplicar o algoritmo de Canny para detecção de bordas
    edges = cv2.Canny(image, 100, 200)

    # Gerar a imagem pontilhista combinando as bordas com pontos menores
    dotted_image = generate_dotted_image(image_color, edges)

    # Salvar e exibir a imagem pontilhista gerada
    cv2.imwrite('cannypoints_image.jpg', dotted_image)
    cv2.imshow('Cannypoints Image', dotted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
•Escolha uma imagem de seu gosto e aplique a técnica que você desenvolveu.
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Detec%C3%A7%C3%A3o%20de%20bordas%20com%20o%20algoritmo%20de%20Canny/resultado.png">
</div>


•Descreva no seu relatório detalhes do procedimento usado para criar sua técnica pontilhista.
#A técnica pontilhista utilizada neste código é um método simples para gerar uma representação pontilhista de uma imagem. O procedimento envolve os seguintes passos:
1. Carregar a imagem de entrada em escala de cinza.
   - O código utiliza a biblioteca OpenCV para ler a imagem passada como argumento para o programa.
2. Converter a imagem em escala de cinza para colorida.
   - A função `cv2.cvtColor` é usada para converter a imagem de escala de cinza para o espaço de cores BGR, necessário para desenhar pontos coloridos posteriormente.
3. Aplicar o algoritmo de detecção de bordas de Canny.
   - O algoritmo de Canny é um método popular para detectar bordas em imagens. Ele utiliza uma combinação de filtros e algoritmos de detecção de bordas para identificar regiões de alta variação de intensidade que correspondem a bordas na imagem.

4. Gerar a imagem pontilhista combinando as bordas com pontos menores.
   - O código utiliza a função `generate_dotted_image` para criar a imagem pontilhista. Essa função recebe a imagem colorida e a imagem das bordas como entrada.
   - Para cada pixel na imagem das bordas, é desenhado um ponto menor na imagem pontilhista. A função `cv2.circle` é utilizada para desenhar círculos de tamanho 2 (diâmetro de 2 pixels) na posição dos pixels de borda.
   - Os pontos são desenhados na imagem pontilhista colorida.

5. Salvar e exibir a imagem pontilhista gerada.
   - A imagem pontilhista resultante é salva em um arquivo chamado "cannypoints_image.jpg" usando a função `cv2.imwrite`.
   - A imagem pontilhista também é exibida em uma janela usando as funções `cv2.imshow`, `cv2.waitKey` e `cv2.destroyAllWindows`.

O resultado final é uma representação pontilhista da imagem original, onde os pontos menores são desenhados nas posições das bordas detectadas pelo algoritmo de Canny.
