from conversao.BGR_RGB import Troca
from conversao.RGB_YIQ_RGB import RGB_YIQ_RGB
from filtros.media import Media
from filtros.sobel import FilterSobel
from filtros.mediana import Mediana

import cv2
import numpy as np

convertRGB = Troca()
convertYIQ = RGB_YIQ_RGB()

path = '/home/skalnark/src/PDI/Trabalho1'
name_img = input("Informe a imagem a ser tratada:")
img_original = cv2.imread('{}/Imagens/{}'.format(path, name_img))
img_original = convertRGB.troca_ordem(img_original)

name_masc = input("Informe a mascara a ser utilizada:")
mascara = cv2.imread('{}/Imagens/{}'.format(path, name_masc))
mascara = convertRGB.troca_ordem(mascara)
# Filtro media
media = Media()
img_filtrada_media = media.correlacao(img_original, 3, 3)
img_filtro_media = '{}/Output/{}_filtro_media.png'.format(path,  name_img)
cv2.imwrite(img_filtro_media, convertRGB.troca_ordem(img_filtrada_media))

# Filtro Sobel
sobel = FilterSobel()
img_filtrada_sobel = sobel.apply_filter_sobel(img_original, 3, 3)
img_filtro_sobel = '{}/Output/{}_filtro_sobel.png'.format(path,  name_img)
cv2.imwrite(img_filtro_sobel, convertRGB.troca_ordem(img_filtrada_sobel))

# Filtro Mediana
mediana = Mediana()
img_yiq = convertYIQ.RGB_TO_YIQ(img_original)
img_filtrada_mediana_yiq = mediana.filtro_mediana_em_y(img_yiq, 3, 3)
img_filtrada_mediana_rgb = convertYIQ.YIQ_TO_RGB(img_filtrada_mediana_yiq)
img_filtro_mediana = '{}/Output/{}_filtro_mediana.png'.format(path,  name_img)
cv2.imwrite(img_filtro_mediana, convertRGB.troca_ordem(img_filtrada_mediana_rgb))

# Correlacao normalizada
correlacao_encontrada = media.correlacao_normalizada(img_original, mascara)
img_correlacao_normalizada = '{}/Output/{}_correlacao_normalizada.png'.format(path,  name_img)
cv2.imwrite(img_correlacao_normalizada, convertRGB.troca_ordem(correlacao_encontrada))