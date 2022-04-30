from turtle import width
import numpy as np
import cv2


class Filtros:
    def filtro_media(self, m, n):
        return np.full((m, n),1/(m*n))


filtro = Filtros()
print(filtro.filtro_media(5, 3))
img_original = cv2.imread('Imagens/{}.png'.format("Woman_eye"))
print(img_original)
