from conversao.BGR_RGB import Troca
from conversao.RGB_YIQ_RGB import RGB_YIQ_RGB
from filtros.sobel import SobelFilter

import cv2
import numpy as np

convertRGB = Troca()
convertYIQ = RGB_YIQ_RGB()

path = 'C:/Users/vanes/Documents/estudos/PDI/Trabalho1'
name_img = input("Informe a imagem a ser tratada:")
img_original = cv2.imread('{}/Imagens/{}'.format(path, name_img))
img_original = convertRGB.troca_ordem(img_original)

# # Filtro Sobel
sobel = SobelFilter()
(img_filtrada_sobel, img_filtrada_sobelx,
 img_filtrada_sobely) = sobel.apply_filter_sobel(img_original)

img_filtro_sobel = '{}/Output/{}_filtro_sobel.png'.format(path,  name_img)
cv2.imwrite(img_filtro_sobel, convertRGB.troca_ordem(img_filtrada_sobel))

img_filtro_sobelx = '{}/Output/{}_filtro_sobelX.png'.format(
    path,  name_img)
cv2.imwrite(img_filtro_sobelx, convertRGB.troca_ordem(img_filtrada_sobelx))

img_filtro_sobely = '{}/Output/{}_filtro_sobelY.png'.format(
    path,  name_img)
cv2.imwrite(img_filtro_sobely, convertRGB.troca_ordem(img_filtrada_sobely))
