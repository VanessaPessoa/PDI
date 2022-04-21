import numpy as np

class BRG_RGB_BRG:
    def BRG_TO_RGB(self, np_image):
        rgb = np.zeros(shape=(33, 44, 3))
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                R = np_image[x, y][2]
                G = np_image[x, y][1]
                B = np_image[x, y][0]
                rgb[x, y] = (R, G, B)
        return rgb

    def RGB_TO_BRG(self, np_image):
        brg = np.zeros(shape=(33, 44, 3))
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                R = np_image[x, y][0]
                G = np_image[x, y][1]
                B = np_image[x, y][2]
                brg[x, y] = (B, G, R)
        return brg
