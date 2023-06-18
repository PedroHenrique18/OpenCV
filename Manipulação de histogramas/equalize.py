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