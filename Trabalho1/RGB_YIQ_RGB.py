import numpy as np

class RGB_YIQ_RGB:
    def RGB_TO_YIQ(self, np_image):
        yiq = np.zeros(shape=(33,44, 3))
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                R = np_image[x, y][0]
                G = np_image[x, y][1]
                B = np_image[x, y][2]


                Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
                I = (0.596 * R) - (0.274 * G) - (0.322 * B)
                Q = (0.211 * R) - (0.523 * G) + (0.312 * B)
                
                yiq[x, y] = (Y, I, Q)
        
        return yiq


    def limit_pixelRGB(self, pixel):
        if pixel > 255:
            return 255.0

        if pixel < 0:
            return 0.0
        
        return pixel

    def YIQ_TO_RGB(self, np_image):
        rgb = np.zeros(shape=(33,44, 3))
        for x in range(0, np_image.shape[0]):
            for y in range(0, np_image.shape[1]):
                Y = np_image[x, y][0]
                I = np_image[x, y][1]
                Q = np_image[x, y][2]

                R = self.limit_pixelRGB((1 * Y) + (0.956 * I) + (0.621 * Q))
                G = self.limit_pixelRGB((1 * Y) - (0.272 * I) - (0.647 * Q))
                B = self.limit_pixelRGB((1 * Y) - (1.106 * I) + (1.703 * Q))
                
                rgb[x, y] = (R, G, B)

        return rgb


