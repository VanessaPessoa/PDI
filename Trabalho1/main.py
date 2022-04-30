import cv2
from RGB_YIQ_RGB import RGB_YIQ_RGB
from BRG_RGB_BRG import BRG_RGB_BRG
from correlacao import Correlacao
from negativo import Negativo
from plt_img import PlotImg

convertRGB_BRG = BRG_RGB_BRG()
convertRGB_YIQ = RGB_YIQ_RGB()
convertNegativo = Negativo()
correlacao = Correlacao()
plt = PlotImg()


try:
    name_img = input("Informe a imagem a ser tratada:")
except:
    print("Imagem nao encontrada")
    name_img = input("Informe a imagem a ser tratada:")

# Carrega imagem em um np
img_original = cv2.imread('Imagens/{}.png'.format(name_img))

# Trocar para RGB
img_color_rgb_original = convertRGB_BRG.troca_ordem(img_original)

# funções com os filtros para correlacao 
mascara = {
    "mediana" : "calcular_media_y_em_pixel"
}

########## 1 Item - Conversão RGB-YIQ-RGB  ##########
img_color_yiq = convertRGB_YIQ.RGB_TO_YIQ(img_color_rgb_original)
cv2.imwrite('Output/{}_yiq.png'.format(name_img),
            convertRGB_BRG.troca_ordem(img_color_yiq))

img_color_rgb = convertRGB_YIQ.YIQ_TO_RGB(img_color_yiq)
cv2.imwrite('Output/{}_yiq_to_rgb.png'.format(name_img),
            convertRGB_BRG.troca_ordem(img_color_rgb))


########## 2 Item - Negativo ##########
plt.plt_img(img_original, "Original RGB")

img_negativo_rgb = 'Output/{}_negativo_rgb.png'.format(name_img)
negativo_rgb = convertNegativo.negativo_RGB(img_color_rgb_original)
cv2.imwrite(img_negativo_rgb, convertRGB_BRG.troca_ordem(negativo_rgb))
plt.plt_img(cv2.imread(img_negativo_rgb), "Negativo em RGB")


img_negativo_Y = 'Output/{}_negativo_Y.png'.format(name_img)
negativo_Y = convertNegativo.negativoBrilho(img_color_yiq)
negativo_Y = convertRGB_YIQ.YIQ_TO_RGB(negativo_Y)
cv2.imwrite(img_negativo_Y, convertRGB_BRG.troca_ordem(negativo_Y))
plt.plt_img(cv2.imread(img_negativo_Y), "Negativo em Y")

#  3 Item

# 4 Item 
filtro_mediana = correlacao.filtro_media_em_y(img_color_yiq, m=3, n=3, filtro = mascara["mediana"])
filtro_mediana = convertRGB_YIQ.YIQ_TO_RGB(filtro_mediana)
img_filtro_mediana = 'Output/{}_filtro_mediana.png'.format(name_img)
cv2.imwrite(img_filtro_mediana, convertRGB_BRG.troca_ordem(filtro_mediana))
