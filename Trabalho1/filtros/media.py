import cv2
import numpy as np


class Media:
    def isPar(self, m, n):
        modulo = (m * n) % 2
        return (1 if modulo == 0 else 0)

    def filtro_media(self, m, n):
        np_masc = np.full((m, n), 1 / (m*n))
        return np_masc

    def correlacao(self, np_img, m, n):
        height = np_img.shape[0]
        width = np_img.shape[1]
        np_img_referencia = np_img.copy()

        np_masc = self.filtro_media(m, n)
        # Desliza pela imagem com a mascara
        for x in range(0, height):
            for y in range(0, width):
                resultado = np.zeros(3, dtype=float)
                contI = 0
                for i in range(x - int(m/2), x + int(m/2) - self.isPar(m, n)):
                    contJ = 0
                    for j in range(y - int(n/2), y + int(n/2) - self.isPar(m, n)):
                        # Verifica se pixel esta entre as bordas
                        if(x < 0 or x >= height or y < 0 or y >= width):
                            pass
                        else:
                            resultado[0] += np_masc[contI, contJ] * np_img[i, j][0]
                            resultado[1] += np_masc[contI, contJ] * np_img[i, j][1]
                            resultado[2] += np_masc[contI, contJ] * np_img[i, j][2]
                        contJ = contJ + 1
                    contI = contI + 1

                np_img_referencia[x, y] = resultado

        return np_img_referencia
