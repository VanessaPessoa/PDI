import cv2
from RGB_YIQ_RGB import RGB_YIQ_RGB
from BRG_RGB_BRG import BRG_RGB_BRG
from correlacao import Correlacao
from negativo import Negativo
import matplotlib.pyplot as plt

convertRGB_BRG = BRG_RGB_BRG()
convertRGB_YIQ = RGB_YIQ_RGB()
convertNegativo = Negativo()
correlacao = Correlacao()

# img_yiq = convertRGB_YIQ.RGB_TO_YIQ(img_rgb)
# img_rgbconvert = convertRGB_YIQ.YIQ_TO_RGB(img_yiq)

# img_eye_yiq_alterado = convertRGB_BRG.change_order(img_yiq)
# cv2.imwrite('Imagens/Woman_eye_YIQ.png', img_eye_yiq_alterado)

# img_eye_rgb_alterado = convertRGB_BRG.change_order(img_rgbconvert)
# cv2.imwrite('Imagens/Woman_eye_RGB.png', img_eye_rgb_alterado)

# # Passar para negativo em RGB
# img_negativo_rgb = convertNegativo.negativo_RGB(img_rgb)
# img_eye__negative_rgb_alterado = convertRGB_BRG.change_order(img_negativo_rgb)
# cv2.imwrite('Imagens/Woman_eye_negative_RGB.png',
#             img_eye__negative_rgb_alterado)


# # Passar Y para negativo
# brilho_negativo = convertNegativo.negativoBrilho(img_yiq)
# brilho_negativo_rgb = convertRGB_YIQ.YIQ_TO_RGB(brilho_negativo)
# brilho_negativo_brg = convertRGB_BRG.change_order(brilho_negativo_rgb)
# cv2.imwrite('Imagens/Woman_eye_negative_L.png', brilho_negativo_brg)

imagem_mulher_filtro = cv2.imread('Imagens/Woman.png')
imagem_mulher_filtro = Correlacao.filtro_media_em_y(imagem_mulher_filtro, m=9, n=9)
cv2.imwrite('Imagens/Woman_filtro_y.png', imagem_mulher_filtro)
