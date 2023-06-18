# 5.2. Exercícios

◉Observando-se o programa labeling.cpp como exemplo, é possível verificar que caso existam mais de 255 objetos na cena, o processo de rotulação poderá ficar comprometido. Identifique a situação em que isso ocorre e proponha uma solução para este problema.

◉Aprimore o algoritmo de contagem apresentado para identificar regiões com ou sem buracos internos que existam na cena. Assuma que objetos com mais de um buraco podem existir. Inclua suporte no seu algoritmo para não contar bolhas que tocam as bordas da imagem. Não se pode presumir, a priori, que elas tenham buracos ou não.
 
 # [labeling.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Preenchendo%20regi%C3%B5es/labeling.py)
```
import cv2
import sys

def main():
    image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("imagem nao carregou corretamente")
        return -1

    width = image.shape[1]
    height = image.shape[0]
    print(f"{width}x{height}")

    p = (0, 0)

    for i in range(height):
        if image[i, width-1] == 255 :
            p = (width-1,i)
            cv2.floodFill(image, None, p, 0)
        if image[i, 0] == 255 :
            p = (0,i)
            cv2.floodFill(image, None, p, 0)
            
    for j in range(width):
        if image[height-1, j] == 255 :
            p = (j,height-1)
            cv2.floodFill(image, None, p, 0)
        if image[0,j] == 255 :
            p = (j,0)
            cv2.floodFill(image, None, p, 0)


    # busca objetos presentes
    nobjects = 0
    for i in range(height):
        for j in range(width):
            if image[i, j] == 255 :
                # achou um objeto
                nobjects += 1
                # para o floodfill as coordenadas
                # x e y são trocadas.
                p = (j, i)
                # preenche o objeto com o contador
                cv2.floodFill(image, None, p, nobjects)


    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    bjects = 0
    for i in range(len(contours)):
        if hierarchy[0, i, 3] == -1:
            # O contorno não possui contornos internos
            # Verifica se há contornos externos para determinar se há um furo
            has_external_contour = hierarchy[0, i, 2] != -1
            if has_external_contour:
                # O objeto tem um furo
                bjects += 1

    print("A figura tem", nobjects, "objetos ",bjects," com furos e" ,nobjects-bjects, "sem furos")
    cv2.imshow("image", image)
    cv2.imwrite("labeling.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

```

Imagem usada
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Preenchendo%20regi%C3%B5es/bolhas.png">
</div>

Imagem após 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Preenchendo%20regi%C3%B5es/labeling.png">
</div>

Saida do console 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Preenchendo%20regi%C3%B5es/resultado.png">
</div>
