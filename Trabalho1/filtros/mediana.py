import numpy as np

class Mediana:

    def isPar(self, m, n):
        modulo = (m * n) % 2
        return (1 if modulo == 0 else 0)

    def filtro_mediana_em_y(self, np_image_yiq, m, n):
        np_image_yiq_referencia = np_image_yiq.copy()
        
        (largura, altura, *_) = np_image_yiq.shape

        for x in range(0, largura):
            for y in range(0, altura):
                np_image_yiq[x, y] = self.calcular_mediana_y_em_pixel(
                    np_image_yiq_referencia, 
                    x,
                    y,
                    m,
                    n,
                    largura,
                    altura)

        return np_image_yiq


    def calcular_mediana_y_em_pixel(self, np_image_yiq, x, y, m, n, largura, altura):
        valoresY = []
        
        for i in range(x - int(m/2), x + int(m/2) - self.isPar(m, n)):
            for j in range(y - int(n/2), y + int(n/2) - self.isPar(m, n)):
                if self.is_pixel_dentro_imagem(i, j, largura, altura):
                    (Y, I, Q) = np_image_yiq[i, j]
                    valoresY.append(Y)

        (_, I, Q) = np_image_yiq[x, y]
        medianaY = np.percentile(Y, 50)

        return (medianaY, I, Q)

    def is_pixel_dentro_imagem(self, x, y, largura, altura):
        if x >= 0 and x < largura and y >= 0 and y < altura:
            return True 
        return False 
