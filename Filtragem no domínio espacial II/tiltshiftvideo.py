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
