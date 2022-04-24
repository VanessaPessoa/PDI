import numpy as np

class BRG_RGB_BRG:
    def  change_order(self, np_image):
        aux = np.zeros(np_image.shape)
        for height in range(0, np_image.shape[0]):
            for width in range(0, np_image.shape[1]):
                (C, B, A) = np_image[height, width]
                aux[height, width] = (C, B, A)
        return aux
