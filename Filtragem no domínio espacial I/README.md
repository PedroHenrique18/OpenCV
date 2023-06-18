# 7.2. Exercícios

◉Utilizando o programa exemplos/filtroespacial.cpp como referência, implemente um programa laplgauss.py. O programa deverá acrescentar mais uma funcionalidade ao exemplo fornecido, permitindo que seja calculado o laplaciano do gaussiano das imagens capturadas. Compare o resultado desse filtro com a simples aplicação do filtro laplaciano.
 
 # [laplgauss.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20no%20dom%C3%ADnio%20espacial%20I/laplgauss.py)
```
import cv2
import numpy as np

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i, j], end=",")
        print("\n")

cap = cv2.VideoCapture(0)  # open the default camera

if not cap.isOpened():  # check if we succeeded
    exit(-1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("largura =", width)
print("altura =", height)
print("fps =", cap.get(cv2.CAP_PROP_FPS))
print("format =", cap.get(cv2.CAP_PROP_FORMAT))

cv2.namedWindow("filtroespacial", cv2.WINDOW_NORMAL)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)

media = np.array([0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111], dtype=np.float32)
gauss = np.array([0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625], dtype=np.float32)
horizontal = np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1], dtype=np.float32)
vertical = np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1], dtype=np.float32)
laplacian = np.array([0, -1, 0, -1, 4, -1, 0, -1, 0], dtype=np.float32)
boost = np.array([0, -1, 0, -1, 5.2, -1, 0, -1, 0], dtype=np.float32)

mask = np.zeros((3, 3), dtype=np.float32)
result_laplacian = np.zeros((height, width), dtype=np.uint8)
result_laplacian_of_gaussian = np.zeros((height, width), dtype=np.uint8)

absolut = 1  # calcs abs of the image

while True:
    ret, frame = cap.read()  # get a new frame from camera
    
    if not ret:
        print("Erro ao capturar o quadro")
        break
    
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    framegray = cv2.flip(framegray, 1)
    
    cv2.imshow("original", framegray)
    
    frame32f = framegray.astype(np.float32)
    
    # Laplaciano
    frameFiltered_laplacian = cv2.filter2D(frame32f, -1, laplacian, borderType=cv2.BORDER_CONSTANT)
    if absolut:
        frameFiltered_laplacian = np.abs(frameFiltered_laplacian)
    
    frameFiltered_laplacian = frameFiltered_laplacian.astype(np.uint8)
    
    cv2.imshow("filtroespacial", frameFiltered_laplacian)
    
    # Laplaciano do Gaussiano
    frameFiltered_log = cv2.GaussianBlur(frame32f, (3, 3), 0)
    frameFiltered_log = cv2.filter2D(frameFiltered_log, -1, laplacian, borderType=cv2.BORDER_CONSTANT)
    if absolut:
        frameFiltered_log = np.abs(frameFiltered_log)
    
    frameFiltered_log = frameFiltered_log.astype(np.uint8)
    
    cv2.imshow("filtroespacial_log", frameFiltered_log)
    
    key = cv2.waitKey(10)
    
    if key == 27:
        break  # esc pressed!
    elif key == ord('a'):
        absolut = not absolut
    elif key == ord('m'):
        mask = media.reshape((3, 3))
        printmask(mask)
    elif key == ord('g'):
        mask = gauss.reshape((3, 3))
        printmask(mask)
    elif key == ord('h'):
        mask = horizontal.reshape((3, 3))
        printmask(mask)
    elif key == ord('v'):
        mask = vertical.reshape((3, 3))
        printmask(mask)
    elif key == ord('l'):
        mask = laplacian.reshape((3, 3))
        printmask(mask)
    elif key == ord('b'):
        mask = boost.reshape((3, 3))
    
cap.release()
cv2.destroyAllWindows()


#Neste código, utilizamos a função cv2.GaussianBlur() para aplicar o 
# filtro Gaussiano antes de realizar a convolução com o filtro 
# laplaciano. O resultado é comparado com a aplicação simples do 
# filtro laplaciano.
```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20no%20dom%C3%ADnio%20espacial%20I/laplgauss.png">
</div>
