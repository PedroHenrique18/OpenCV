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
