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