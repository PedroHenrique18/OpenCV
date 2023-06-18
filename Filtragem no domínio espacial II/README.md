# 8.1. Exercícios

◉Utilizando o programa exemplos/addweighted.cpp como referência, implemente um programa tiltshift.py. Três ajustes deverão ser providos na tela da interface:

um ajuste para regular a altura da região central que entrará em foco;

um ajuste para regular a força de decaimento da região borrada;

um ajuste para regular a posição vertical do centro da região que entrará em foco. Finalizado o programa, a imagem produzida deverá ser salva em arquivo.


 
 # [tiltshift.py](https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20no%20dom%C3%ADnio%20espacial%20II/tiltshift.py)
```
import cv2

def on_trackbar_blend(val):
    global alpha
    alpha = val / alpha_slider_max
    blended = cv2.addWeighted(image1, 1-alpha, imageTop, alpha, 0.0)
    cv2.imshow("addweighted", blended)

def on_trackbar_line(val):
    global imageTop
    imageTop = image2.copy()
    limit = int(val * image_height / top_slider_max)
    if limit > 0:
        alpha = limit / image_height
        cv2.addWeighted(image2[0:limit, :], alpha, image1[0:limit, :], 1-alpha, 0, imageTop[0:limit, :])
    on_trackbar_blend(alfa_slider)

def on_trackbar_height(val):
    global image_height
    image_height = int(val * image1.shape[0] / height_slider_max)
    on_trackbar_line(top_slider)

def on_trackbar_decay(val):
    global alpha_slider_max
    alpha_slider_max = val
    on_trackbar_blend(alfa_slider)

def on_trackbar_position(val):
    global top_slider_max
    top_slider_max = val
    on_trackbar_line(top_slider)

alfa = 0.0
alfa_slider = 0
alfa_slider_max = 100
top_slider = 0
top_slider_max = 100
height_slider = 0
height_slider_max = 100
alpha_slider_max = 255

image1 = cv2.imread("blend1.jpg")
image2 = cv2.imread("blend2.jpg")
imageTop = image2.copy()
image_height = image1.shape[0]

cv2.namedWindow("addweighted")

cv2.createTrackbar("Alpha x {}".format(alfa_slider_max), "addweighted", alfa_slider, alfa_slider_max, on_trackbar_blend)
cv2.createTrackbar("Scanline x {}".format(top_slider_max), "addweighted", top_slider, top_slider_max, on_trackbar_line)
cv2.createTrackbar("Height x {}".format(height_slider_max), "addweighted", height_slider, height_slider_max, on_trackbar_height)
cv2.createTrackbar("Decay x {}".format(alpha_slider_max), "addweighted", alpha_slider_max, 255, on_trackbar_decay)
cv2.createTrackbar("Position x {}".format(top_slider_max), "addweighted", top_slider_max, 100, on_trackbar_position)

on_trackbar_blend(alfa_slider)
on_trackbar_line(top_slider)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Salvar imagem produzida em arquivo
blended_filename = "blended_image.jpg"
cv2.imwrite(blended_filename, imageTop)
print("Imagem produzida salva como", blended_filename)
```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20no%20dom%C3%ADnio%20espacial%20II/tiltshift.png">
</div>


◉Utilizando o programa exemplos/addweighted.cpp como referência, implemente um programa tiltshiftvideo.py. Tal programa deverá ser capaz de processar um arquivo de vídeo, produzir o efeito de tilt-shift nos quadros presentes e escrever o resultado em outro arquivo de vídeo. A ideia é criar um efeito de miniaturização de cenas. Descarte quadros em uma taxa que julgar conveniente para evidenciar o efeito de stop motion, comum em vídeos desse tipo.

# trocaregioes.py
```
import cv2
import numpy as np

def apply_tilt_shift(frame):
    # Obter as dimensões do quadro
    height, width = frame.shape[:2]

    # Definir a proporção da região de foco
    focus_ratio = 0.4

    # Definir as regiões superior e inferior a serem desfocadas
    top_region = int(height * focus_ratio)
    bottom_region = int(height * (1 - focus_ratio))

    # Aplicar desfoque às regiões superior e inferior
    blurred_frame = frame.copy()
    blurred_frame[:top_region, :] = cv2.GaussianBlur(frame[:top_region, :], (0, 0), sigmaX=30)
    blurred_frame[bottom_region:, :] = cv2.GaussianBlur(frame[bottom_region:, :], (0, 0), sigmaX=30)

    # Mesclar o quadro original com o quadro desfocado
    processed_frame = cv2.addWeighted(frame, 1.0, blurred_frame, 0.8, 0)

    return processed_frame

def process_video(input_file, output_file, discard_rate):
    # Abrir o arquivo de vídeo de entrada
    video_capture = cv2.VideoCapture(input_file)

    # Obter as dimensões do vídeo de entrada
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Criar o objeto para escrever o arquivo de vídeo de saída
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec de vídeo para o arquivo de saída
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    frame_count = 0

    while True:
        # Ler o próximo quadro do vídeo de entrada
        ret, frame = video_capture.read()

        if not ret:
            break

        frame_count += 1

        # Descartar quadros com base na taxa de descarte
        if frame_count % discard_rate != 0:
            continue

        # Aplicar o efeito de tilt-shift no quadro
        processed_frame = apply_tilt_shift(frame)

        # Escrever o quadro processado no arquivo de vídeo de saída
        video_writer.write(processed_frame)

    # Liberar os recursos
    video_capture.release()
    video_writer.release()

input_file = "meuvideo.mp4"
output_file = "output_video.mp4"
discard_rate = 2  # Taxa de descarte de quadros (descartar a cada 2 quadros)

process_video(input_file, output_file, discard_rate)

```

<div align="center" >
  <img src="https://github.com/PedroHenrique18/OpenCV/blob/main/Filtragem%20no%20dom%C3%ADnio%20espacial%20II/output_gif.gif">
</div>
