import numpy as np


class Negativo:
    def negativo(self, pixel):
        return 255 - pixel

    def negativo_RGB(self, np_img):
        neg_img = np.zeros(np_img.shape)
        for height in range(0, np_img.shape[0]):
            for width in range(0, np_img.shape[1]):
                R = self.negativo(np_img[height, width][0])
                G = self.negativo(np_img[height, width][1])
                B = self.negativo(np_img[height, width][2])

                neg_img[height, width] = (R, G, B)
        return neg_img

    def negativoBrilho(self, np_img):
        neg_img = np.zeros(np_img.shape)
        for height in range(0, np_img.shape[0]):
            for width in range(0, np_img.shape[1]):
                Y = self.negativo(np_img[height, width][0])
                I = np_img[height, width][1]
                Q = np_img[height, width][2]
                neg_img[height, width] = (Y, I, Q)
        return neg_img
