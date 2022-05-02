import numpy as np
import matplotlib.pyplot as plt
import cv2


class SobelFilter():
    def __init__(self) -> None:
        self.sobelx = np.array(
            [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float)
        self.sobely = np.array(
            [[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float)

    def isPar(self, m, n):
        modulo = (m * n) % 2
        return (1 if modulo == 0 else 0)

    def apply_filter_sobel(self, np_img):
        height = np_img.shape[0]
        width = np_img.shape[1]
        np_img_referencia = np_img.copy()
        sobelx = np_img.copy()
        sobely = np_img.copy()

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

                gx = np.absolute(gx)
                sobelx[x-1][y-1] = gx

                gy = np.absolute(gy)
                sobely[x-1][y-1] = gy

                g = gx + gy 
                np_img_referencia[x-1][y-1] = g
        return (np_img_referencia, sobelx, sobely)
