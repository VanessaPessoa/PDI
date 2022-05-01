from re import S
import numpy as np


class FilterSobel():
    def __init__(self) -> None:
        self.sobelx = np.array(
            [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float)
        self.sobely = np.array(
            [[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float)

    def isPar(self, m, n):
        modulo = (m * n) % 2
        return (1 if modulo == 0 else 0)

    def calculate_gx_gy(self, np_img, np_masc, i, j, contI, contJ):
        resultado = np.zeros(3, dtype=float)

        resultado[0] += np_masc[contI, contJ] * np_img[i, j][0]
        resultado[1] += np_masc[contI, contJ] * np_img[i, j][1]
        resultado[2] += np_masc[contI, contJ] * np_img[i, j][2]
        contJ = contJ + 1
        contI = contI + 1

        return resultado

        
    def apply_filter_sobel(self, np_img, m, n):
        height = np_img.shape[0]
        width = np_img.shape[1]
        np_img_referencia = np_img.copy()
        sobelxImage = np.zeros((height,width))
        sobelyImage = np.zeros((height,width))

        # Desliza pela imagem com a mascara
        for x in range(0, height-1):
            for y in range(0, width-1):
                gx = (self.sobelx[0][0] * np_img[x-1][y-1]) + (self.sobelx[0][1] * np_img[x-1][y]) + \
                (self.sobelx[0][2] * np_img[x-1][y+1]) + (self.sobelx[1][0] * np_img[x][y-1]) + \
                (self.sobelx[1][1] * np_img[x][y]) + (self.sobelx[1][2] * np_img[x][y+1]) + \
                (self.sobelx[2][0] * np_img[x+1][y-1]) + (self.sobelx[2][1] * np_img[x+1][y]) + \
                (self.sobelx[2][2] * np_img[x+1][y+1])

                gy = (self.sobely[0][0] * np_img[x-1][y-1]) + (self.sobely[0][1] * np_img[x-1][y]) + \
                    (self.sobely[0][2] * np_img[x-1][y+1]) + (self.sobely[1][0] * np_img[x][y-1]) + \
                    (self.sobely[1][1] * np_img[x][y]) + (self.sobely[1][2] * np_img[x][y+1]) + \
                    (self.sobely[2][0] * np_img[x+1][y-1]) + (self.sobely[2][1] * np_img[x+1][y]) + \
                    (self.sobely[2][2] * np_img[x+1][y+1])     

                # sobelxImage[x-1][y-1] = gx
                # sobelyImage[x-1][y-1] = gy
                g = np.sqrt(gx * gx + gy * gy)
                np_img_referencia[x-1][y-1] = g

        return np_img_referencia
