import numpy as np


class Negativo:
    def negativo(self, pixel):
        return 255 - pixel

    def negativo_RGB(self, np_img):
        neg_img = np.zeros(np_img.shape)
        for x in range(0, np_img.shape[0]):
            for y in range(0, np_img.shape[1]):
                R = self.negativo(np_img[x, y][0])
                G = self.negativo(np_img[x, y][1])
                B = self.negativo(np_img[x, y][2])

                neg_img[x, y] = (R, G, B)
        return neg_img

