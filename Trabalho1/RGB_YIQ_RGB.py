import numpy as np


class RGB_YIQ_RGB:

    @staticmethod
    def RGB_TO_YIQ(np_image):
        yiq = np.zeros(np_image.shape)
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                (R, G, B) = np_image[x, y]

                Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
                I = (0.596 * R) - (0.274 * G) - (0.322 * B)
                Q = (0.211 * R) - (0.523 * G) + (0.312 * B)

                yiq[x, y] = (Y, I, Q)

        return yiq

    @staticmethod
    def limite_componente_rgb(pixel):
        if pixel > 255:
            return 255.0

        if pixel < 0:
            return 0.0

        return pixel

    @staticmethod
    def YIQ_TO_RGB(np_image):
        rgb = np.zeros(np_image.shape)
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                (Y, I, Q) = np_image[x, y]

                R = RGB_YIQ_RGB.limite_componente_rgb((1 * Y) + (0.956 * I) + (0.621 * Q))
                G = RGB_YIQ_RGB.limite_componente_rgb((1 * Y) - (0.272 * I) - (0.647 * Q))
                B = RGB_YIQ_RGB.limite_componente_rgb((1 * Y) - (1.106 * I) + (1.703 * Q))

                rgb[x, y] = (R, G, B)

        return rgb
