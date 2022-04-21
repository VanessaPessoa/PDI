import cv2
from RGB_YIQ_RGB import RGB_YIQ_RGB
from BRG_RGB_BRG import BRG_RGB_BRG
from negativo import Negativo
import matplotlib.pyplot as plt 


def plt_img(img):
    color = ('b', 'g', 'r') 
    
    for i, col in enumerate(color): 
        histr = cv2.calcHist([img],  
                            [i], None, 
                            [255],  
                            [0, 255]) 
        plt.plot(histr, color = col) 
        plt.xlim([0, 256]) 
    plt.show() 

convertRGB_BRG = BRG_RGB_BRG()
convertRGB_YIQ = RGB_YIQ_RGB()
convertNegativo = Negativo()

img_eye = cv2.imread('Imagens/Woman_eye.png')
img_rgb = convertRGB_BRG.BRG_TO_RGB(img_eye)


img_yiq = convertRGB_YIQ.RGB_TO_YIQ(img_rgb)
img_rgbconvert = convertRGB_YIQ.YIQ_TO_RGB(img_yiq)

img_eye_yiq_alterado = convertRGB_BRG.RGB_TO_BRG(img_yiq)
cv2.imwrite('Imagens/Woman_eye_YIQ.png', img_eye_yiq_alterado)

img_eye_rgb_alterado = convertRGB_BRG.RGB_TO_BRG(img_rgbconvert)
cv2.imwrite('Imagens/Woman_eye_RGB.png', img_eye_rgb_alterado)

