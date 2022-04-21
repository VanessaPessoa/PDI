import cv2
import numpy as np


class Correlacao:
    def filtro_media(self, np_img):
        fator = (np_img.shape[2])
        h = 1 / (fator * fator)
        np_media = np.full((fator, fator), h)
        print(np_media)

img_eye = cv2.imread('Imagens/Woman.png')
correlacao = Correlacao()
correlacao.filtro_media(img_eye)
