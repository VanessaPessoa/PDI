from conversao.BGR_RGB import Troca
from conversao.RGB_YIQ_RGB import RGB_YIQ_RGB
from filtros.correlacaoNormalizada import Normalizada

import cv2
import numpy as np

convertRGB = Troca()
convertYIQ = RGB_YIQ_RGB()

path = 'C:/Users/vanes/Documents/estudos/PDI/Trabalho1'
name_img = input("Informe a imagem a ser tratada:")
img_original = cv2.imread('{}/Imagens/{}'.format(path, name_img))
img_original = convertRGB.troca_ordem(img_original)

name_masc = input("Informe a mascara a ser utilizada:")
mascara = cv2.imread('{}/Imagens/{}'.format(path, name_masc))
mascara = convertRGB.troca_ordem(mascara)

media = Normalizada()

correlacao_encontrada = media.correlacao_normalizada(img_original, mascara)
img_correlacao_normalizada = '{}/Output/{}_correlacao_normalizada.png'.format(path,  name_img)
cv2.imwrite(img_correlacao_normalizada, convertRGB.troca_ordem(correlacao_encontrada))