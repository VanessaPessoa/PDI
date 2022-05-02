from conversao.BGR_RGB import Troca
from conversao.RGB_YIQ_RGB import RGB_YIQ_RGB
from filtros.mediana import MedianFilter

import cv2
import numpy as np

convertRGB = Troca()
convertYIQ = RGB_YIQ_RGB()

path = 'C:/Users/vanes/Documents/estudos/PDI/Trabalho1'
name_img = input("Informe a imagem a ser tratada:")
img_original = cv2.imread('{}/Imagens/{}'.format(path, name_img))
img_original = convertRGB.troca_ordem(img_original)

mediana = MedianFilter()
img_yiq = convertYIQ.RGB_TO_YIQ(img_original)
img_filtrada_mediana_yiq = mediana.apply_filter_median(img_yiq, 11, 11)
img_filtrada_mediana_rgb = convertYIQ.YIQ_TO_RGB(img_filtrada_mediana_yiq)
img_filtro_mediana = '{}/Output/{}_filtro_mediana.png'.format(
    path,  name_img)
cv2.imwrite(img_filtro_mediana, convertRGB.troca_ordem(
    img_filtrada_mediana_rgb))
