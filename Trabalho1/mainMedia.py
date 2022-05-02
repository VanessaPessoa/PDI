from conversao.BGR_RGB import Troca
from conversao.RGB_YIQ_RGB import RGB_YIQ_RGB
from filtros.media import MediaFilter

import cv2
import numpy as np

convertRGB = Troca()
convertYIQ = RGB_YIQ_RGB()

path = 'C:/Users/vanes/Documents/estudos/PDI/Trabalho1'
name_img = input("Informe a imagem a ser tratada:")
img_original = cv2.imread('{}/Imagens/{}'.format(path, name_img))
img_original = convertRGB.troca_ordem(img_original)

# Filtro media
media = MediaFilter()
img_filtrada_media = media.apply_filter_media(img_original, 3, 3)
img_filtro_media = '{}/Output/{}_filtro_media.png'.format(path,  name_img)
cv2.imwrite(img_filtro_media, convertRGB.troca_ordem(img_filtrada_media))