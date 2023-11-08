import cv2
import numpy as np

# Cargar una imagen
img = cv2.imread(r"C:\Users\M413UA\Documents\ISABELLA\Catedra\Material_info\Info-2\Unidad 2\OpenCV\brain.png", cv2.IMREAD_COLOR)

# Mostrar la imagen original
cv2.imshow('Imagen Original', img)

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow('Imagen en Grises', gris)

# Aplicar un filtro Gaussiano para reducir ruido
img_filtrada = cv2.GaussianBlur(gris, (5, 5), 0)

# Mostrar la imagen filtrada
cv2.imshow('Imagen Filtrada', img_filtrada)

# Detectar bordes utilizando el operador de Canny
bordes = cv2.Canny(img_filtrada, 100, 200)

# Mostrar los bordes detectados
cv2.imshow('Bordes Detectados', bordes)

# Esperar a que se presione una tecla y cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()


