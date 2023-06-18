import cv2
import sys
import numpy as np

def run_kmeans(image_path, output_prefix):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Erro ao abrir a imagem: {image_path}")
        return

    samples = img.reshape(-1, 3).astype(np.float32)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)
    flags = cv2.KMEANS_RANDOM_CENTERS
    n_rounds = 10

    for i in range(n_rounds):
        _, labels, centers = cv2.kmeans(samples, 8, None, criteria, 1, flags)

        segmented_image = centers[labels.flatten()].reshape(img.shape)
        output_filename = f"{output_prefix}_{i+1}.jpg"
        cv2.imwrite(output_filename, segmented_image)

    print("Processamento concluído.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python kmeans.py <caminho_imagem> <prefixo_saida>")
        sys.exit()

    image_path = sys.argv[1]
    output_prefix = sys.argv[2]

    run_kmeans(image_path, output_prefix)





#As diferentes imagens produzidas em cada rodada do algoritmo K-means
#  podem diferir bastante devido a dois fatores principais: inicialização
#  aleatória dos centros e sensibilidade a valores iniciais.

#Inicialização aleatória dos centros: O algoritmo K-means inicia os 
# centros de cluster de forma aleatória em cada rodada. Isso significa
#  que a posição inicial dos centros pode variar de uma execução para 
# outra. Como o algoritmo busca convergir para uma solução ótima, as 
# diferentes posições iniciais dos centros podem levar a diferentes 
# agrupamentos. Dependendo da inicialização aleatória, os centros podem
#  ser posicionados em regiões diferentes do espaço de características,
#  resultando em diferentes agrupamentos finais.

#Sensibilidade a valores iniciais: O algoritmo K-means é sensível aos 
# valores iniciais dos centros. Pequenas alterações na posição inicial 
# dos centros podem levar a diferentes iterações e agrupamentos finais. 
# Isso ocorre porque o algoritmo segue um processo iterativo para 
# atualizar os centros e as atribuições dos pontos aos clusters. 
# Se os centros iniciais estiverem próximos de alguns pontos específicos,
#  esses pontos podem ser atraídos para um cluster específico, 
# influenciando o resultado final. Portanto, diferentes valores iniciais
#  podem levar a diferentes resultados finais.

#Esses fatores combinados fazem com que as imagens segmentadas variem 
# em cada rodada do algoritmo K-means. A inicialização aleatória e a 
# sensibilidade a valores iniciais resultam em diferentes posições dos 
# centros e diferentes atribuições de pontos aos clusters, o que leva 
# a diferentes agrupamentos e, consequentemente, a diferentes imagens 
# segmentadas.











