import numpy as np

class BRG_RGB_BRG:
    def BRG_TO_RGB(self, np_image):
        rgb = np.zeros(np_image.shape)
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                (B, G, R) = np_image[x, y]
                rgb[x, y] = (R, G, B)
        return rgb

    def RGB_TO_BRG(self, np_image):
        brg = np.zeros(np_image.shape)
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                (R, G, B) = np_image[x, y]
                brg[x, y] = (B, G, R)
        return brg
