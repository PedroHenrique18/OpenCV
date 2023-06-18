import cv2
import numpy as np
import sys

def swap_quadrants(image):
    tmp = np.copy(image)
    cx = image.shape[1] // 2
    cy = image.shape[0] // 2

    # Swap quadrants (Top-Left with Bottom-Right)
    tmp[:cy, :cx], image[cy:, cx:] = image[cy:, cx:], tmp[:cy, :cx].copy()

    # Swap quadrant (Top-Right with Bottom-Left)
    tmp[:cy, cx:], image[cy:, :cx] = image[cy:, :cx], tmp[:cy, cx:].copy()

def make_filter(image):
    filter2D = np.zeros_like(image, dtype=np.float32)
    centerX = image.shape[1] // 2
    centerY = image.shape[0] // 2
    radius = 20

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (i - centerY) ** 2 + (j - centerX) ** 2 <= radius ** 2:
                filter2D[i, j] = 1

    return filter2D

def homomorphic_filter(image, cutoff_freq, boost):
    # Convert image to float32 for the subsequent calculations
    image = image.astype(np.float32)

    # Apply logarithmic transformation to enhance the dynamic range of the image
    image_log = np.log1p(image)

    # Perform the DFT on the log-transformed image
    dft_M = cv2.getOptimalDFTSize(image_log.shape[0])
    dft_N = cv2.getOptimalDFTSize(image_log.shape[1])
    padded = cv2.copyMakeBorder(image_log, 0, dft_M - image_log.shape[0], 0, dft_N - image_log.shape[1], cv2.BORDER_CONSTANT, value=0)
    complexImage = np.zeros((padded.shape[0], padded.shape[1], 2), dtype=np.float32)
    complexImage[:, :, 0] = padded
    complexImage = cv2.dft(complexImage)
    swap_quadrants(complexImage)

    # Create the homomorphic filter
    filter = make_filter(image)
    filter = (1 - boost) + boost * filter
    filter = cv2.GaussianBlur(filter, (0, 0), cutoff_freq)
    filter = np.clip(filter, 0.01, 1)

    # Apply the homomorphic filter in the frequency domain
    filtered_image = complexImage * np.expand_dims(filter, axis=2)

    # Perform the inverse DFT
    swap_quadrants(filtered_image)
    filtered_image = cv2.idft(filtered_image)

    # Separate the real and imaginary components
    planos = cv2.split(filtered_image)

    # Normalize and apply exponential minus one
    min_value = np.min(planos[0])
    max_value = np.max(planos[0])
    result = (planos[0] - min_value) / (max_value - min_value)

    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Informe o caminho para a imagem de entrada.")
        exit()

    image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Erro ao abrir a imagem", sys.argv[1])
        exit()

    # Define the parameters for the homomorphic filter
    cutoff_freq = 30
    boost = 1.0

    # Apply the homomorphic filter to the image
    result = homomorphic_filter(image, cutoff_freq, boost)

    # Display the resulting image
    cv2.imshow("image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
