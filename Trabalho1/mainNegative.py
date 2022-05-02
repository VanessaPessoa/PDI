from conversao.BGR_RGB import Troca
from conversao.RGB_YIQ_RGB import RGB_YIQ_RGB
from filtros.negativo import Negativo

import cv2
import numpy as np

convertRGB = Troca()
convertYIQ = RGB_YIQ_RGB()
filter = Negativo()

path = 'C:/Users/vanes/Documents/estudos/PDI/Trabalho1'
name_img = input("Informe a imagem a ser tratada:")
img_original = cv2.imread('{}/Imagens/{}'.format(path, name_img))
img_original = convertRGB.troca_ordem(img_original)

img_negativo_rgb = '{}/Output/{}_negativo_rgb.png'.format(path,name_img)
negativo_rgb = filter.negativo_RGB(img_original)
cv2.imwrite(img_negativo_rgb, convertRGB.troca_ordem(negativo_rgb))

img_yiq = convertYIQ.RGB_TO_YIQ(img_original)
img_negativo_Y = '{}/Output/{}_negativo_Y.png'.format(path, name_img)
negativo_Y = filter.negativoBrilho(img_yiq)
negativo_Y_rgb = convertYIQ.YIQ_TO_RGB(negativo_Y)
cv2.imwrite(img_negativo_Y, convertRGB.troca_ordem(negativo_Y_rgb))
