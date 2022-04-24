import re
import cv2
import numpy as np
from RGB_YIQ_RGB import RGB_YIQ_RGB

class Correlacao:

    @staticmethod
    def filtro_media_em_y(np_image_rgb, m, n):
        np_image_yiq = RGB_YIQ_RGB.RGB_TO_YIQ(np_image_rgb)
        np_image_yiq_referencia = np_image_yiq.copy()
        
        (largura, altura, *_) = np_image_yiq.shape

        for x in range(0, largura):
            for y in range(0, altura):
                np_image_yiq[x, y] = Correlacao.calcular_media_y_em_pixel(
                    np_image_yiq_referencia, 
                    x,
                    y,
                    m,
                    n,
                    largura,
                    altura)

        return RGB_YIQ_RGB.YIQ_TO_RGB(np_image_yiq)


    @staticmethod
    def calcular_media_y_em_pixel(np_image_yiq, x, y, m, n, largura, altura):
        somaY = 0
        somaI = 0
        somaQ = 0
        
        for i in range(x - int(m/2), x + int(m/2)):
            for j in range(y - int(n/2), y + int(n/2)):
                if Correlacao.is_pixel_dentro_imagem(i, j, largura, altura):
                    (Y, I, Q) = np_image_yiq[i, j]
                    somaY = somaY + Y
                    somaI = somaI + I
                    somaQ = somaQ + Q

        (_, I, Q) = np_image_yiq[x, y]
        mediaY = somaY / (m * n)
        mediaI = somaI / (m * n)
        mediaQ = somaQ / (m * n)

        return (mediaY, I, Q)

    @staticmethod
    def is_pixel_dentro_imagem(x, y, largura, altura) -> bool:
        if x >= 0 and x < largura and y >= 0 and y < altura:
            return True 
        return False 
