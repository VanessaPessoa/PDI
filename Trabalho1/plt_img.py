import matplotlib.pyplot as plt
import cv2

class PlotImg:
    def plt_img(self, img, msg):
        color = ('b', 'g', 'r')

        for i, col in enumerate(color):
            histr = cv2.calcHist([img],
                                [i], None,
                                [255],
                                [0, 255])
            plt.plot(histr, color=col)
            plt.title(msg)
            plt.xlim([0, 256])
        plt.show()
