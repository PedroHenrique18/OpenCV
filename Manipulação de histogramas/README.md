# 6.2. Exercícios

◉Utilizando o programa exemplos/histogram.cpp como referência, implemente um programa equalize.py. Este deverá, para cada imagem capturada, realizar a equalização do histogram antes de exibir a imagem. Teste sua implementação apontando a câmera para ambientes com iluminações variadas e observando o efeito gerado. Assuma que as imagens processadas serão em tons de cinza.
 
 # [equalize.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Manipula%C3%A7%C3%A3o%20de%20histogramas/equalize.py)
```
import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Câmera indisponível")
        return -1
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print("largura =", width)
    print("altura =", height)
    
    nbins = 64
    range_ = [0, 256]
    histrange = [range_]
    uniform = True
    accumulate = False
    
    histw = nbins
    histh = int(nbins / 2)
    histImgR = np.zeros((histh, histw, 3), dtype=np.uint8)
    histImgG = np.zeros((histh, histw, 3), dtype=np.uint8)
    histImgB = np.zeros((histh, histw, 3), dtype=np.uint8)
    
    while True:
        ret, image = cap.read()
        
        if not ret:
            print("Erro ao capturar o quadro")
            break
        
        planes = cv2.split(image)
        
        # Equalizar o histograma para cada canal de cor
        eq_planes = []
        for plane in planes:
            eq_plane = cv2.equalizeHist(plane)
            eq_planes.append(eq_plane)
        
        histB = cv2.calcHist([eq_planes[0]], [0], None, [nbins], range_, accumulate=accumulate)
        histG = cv2.calcHist([eq_planes[1]], [0], None, [nbins], range_, accumulate=accumulate)
        histR = cv2.calcHist([eq_planes[2]], [0], None, [nbins], range_, accumulate=accumulate)
        
        cv2.normalize(histR, histR, 0, histImgR.shape[0], cv2.NORM_MINMAX, -1)
        cv2.normalize(histG, histG, 0, histImgG.shape[0], cv2.NORM_MINMAX, -1)
        cv2.normalize(histB, histB, 0, histImgB.shape[0], cv2.NORM_MINMAX, -1)
        
        histImgR.fill(0)
        histImgG.fill(0)
        histImgB.fill(0)
        
        for i in range(nbins):
            cv2.line(histImgR, (i, histh), (i, histh - int(histR[i])), (0, 0, 255), 1, 8, 0)
            cv2.line(histImgG, (i, histh), (i, histh - int(histG[i])), (0, 255, 0), 1, 8, 0)
            cv2.line(histImgB, (i, histh), (i, histh - int(histB[i])), (255, 0, 0), 1, 8, 0)
        
        image[0:histh, 0:nbins] = histImgR
        image[histh:2*histh, 0:nbins] = histImgG
        image[2*histh:3*histh, 0:nbins] = histImgB
        
        cv2.imshow("image", image)
        key = cv2.waitKey(30)
        if key == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


    #Este código captura os quadros da câmera, 
    # converte cada quadro para tons de cinza usando cv2.cvtColor, 
    # em seguida, aplica a equalização do histograma usando 
    # cv2.equalizeHist e exibe a imagem resultante. Certifique-se 
    # de ter o OpenCV instalado corretamente e execute o código 
    # para observar o efeito da equalização do histograma em diferentes 
    # ambientes com iluminações variadas.
```
Sem equalização
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Manipula%C3%A7%C3%A3o%20de%20histogramas/sem%20equaliza%C3%A7%C3%A3o.png">
</div>
Com equalização 
<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Manipula%C3%A7%C3%A3o%20de%20histogramas/equaliza%C3%A7%C3%A3o%20do%20histogram.png">
</div>

◉Utilizando o programa exemplos/histogram.cpp como referência, implemente um programa motiondetector.py. Este deverá continuamente calcular o histograma da imagem (apenas uma componente de cor é suficiente) e compará-lo com o último histograma calculado. Quando a diferença entre estes ultrapassar um limiar pré-estabelecido, ative um alarme. Utilize uma função de comparação que julgar conveniente.

# [motiondetector.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Manipula%C3%A7%C3%A3o%20de%20histogramas/motiondetector.py)
```
import cv2
import numpy as np

def histogram_difference(hist1, hist2):
    # Função para calcular a diferença entre dois histogramas
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Câmera indisponível")
        return -1
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print("largura =", width)
    print("altura =", height)
    
    nbins = 64
    range_ = [0, 256]
    histrange = [range_]
    uniform = True
    accumulate = False
    
    hist_last = None
    threshold = 0.5
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Erro ao capturar o quadro")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        hist = cv2.calcHist([gray], [0], None, [nbins], range_, accumulate=accumulate)
        
        if hist_last is not None:
            difference = histogram_difference(hist, hist_last)
            
            if difference > threshold:
                cv2.putText(frame, "ALERTA! Movimento detectado", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        hist_last = hist
        
        cv2.imshow("image", frame)
        key = cv2.waitKey(30)
        if key == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


#Neste código, adicionamos a função histogram_difference para calcular 
# a diferença entre dois histogramas usando cv2.compareHist. Durante o 
# loop principal, calculamos continuamente o histograma de uma 
# componente de cor da imagem (convertida para tons de cinza) e 
# comparamos com o último histograma calculado. Se a diferença entre 
# os histogramas ultrapassar o limiar especificado, um alarme é ativado.
# Certifique-se de ter o OpenCV instalado corretamente e execute o 
# código para observar o alarme sendo ativado quando ocorrer uma 
# diferença significativa no histograma.
```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Manipula%C3%A7%C3%A3o%20de%20histogramas/semmovimento.png">
</div>

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Manipula%C3%A7%C3%A3o%20de%20histogramas/movimentodetectado.png">
</div>
