import numpy as np


class Normalizada:

    def isPar(self, m, n):
        modulo = (m * n) % 2
        return (1 if modulo == 0 else 0)


    def correlacao_normalizada(self, np_img, np_masc):
        height = np_img.shape[0]
        width = np_img.shape[1]
        m = np_masc.shape[0]
        n = np_masc.shape[1]
        
        npg_img = self._gray_scale(np_img)
        
        npg_masc = self._gray_scale(np_masc)
        npg_masc = self._rebater_img(npg_masc)

        media_masc = self._media_pearson_simplificada(npg_masc)
        mascara = self._correlacao_normalizada_simplificado(npg_masc, media_masc)

        maior_correl_pos = -1
        maior_correl_neg = 1

        px_correl_pos = 0
        py_correl_pos = 0
        px_correl_neg = 0
        py_correl_neg = 0

        # Desliza pela imagem com a mascara
        for x in range(0, height):

            print("Linha: " + str(x))
            rangeImin = x - int(m/2)
            rangeIMax = x + int(m/2) - self.isPar(m, n)
            for y in range(0, width):
                rangeJmin = y - int(n/2)
                rangeJMax = y + int(n/2) - self.isPar(m, n)

                contI = 0

                for i in range(rangeImin, rangeIMax):

                    contJ = 0
                    ultima_correlacao = 0

                    for j in range(rangeJmin, rangeJMax):
                        # Verifica se pixel esta entre as bordas
                        if(x < 0 or x >= height or y < 0 or y >= width or
                           i < 0 or i >= height or j < 0 or j >= width):
                            pass
                        else:
                            media_img = self._media_pearson(npg_img, i, j, m, n)
                            ultima_correlacao = self._correlacao_normalizada(npg_img, i, j, m, n, media_img) * mascara

                            if(ultima_correlacao > maior_correl_pos):
                                maior_correl_pos = ultima_correlacao
                                px_correl_pos = j 
                                py_correl_pos = i
                            if(ultima_correlacao < maior_correl_neg):
                                maior_correl_neg = ultima_correlacao
                                px_correl_neg = j
                                py_correl_neg = i

                        contJ = contJ + 1
                    contI = contI + 1

        return self._destacar_correlacao(np_img, px_correl_pos, py_correl_pos, px_correl_neg, py_correl_neg, m, n)


    
    def _rebater_img(self, np_img):
        height = np_img.shape[0]
        width = np_img.shape[1]
        np_img_referencia = np_img.copy()
        for x in range(height, 0):
            for y in range(width, 0):
               np_img_referencia[height - x][width - y][0] = np_img[x, y][0]
        return np_img_referencia
    
    def _gray_scale(self, img):
        altura = img.shape[0]
        largura = img.shape[1]

        gray_img = np.zeros(img.shape)
        for i in range(0, altura):
            for j in range(0, largura):
                R = img[i, j][0]
                G = img[i, j][1]
                B = img[i, j][2]

                Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
                gray_img[i, j] = (Y, Y, Y)
        return gray_img
    
    def _media_pearson(self, npg_img, x, y, m, n):
        height = npg_img.shape[0]
        width = npg_img.shape[1]
        soma = 0
        
        for i in range(x - int(m/2), x + int(m/2) - self.isPar(m, n) - 1):
            for j in range(y - int(n/2), y + int(n/2) - self.isPar(m, n) - 1):
                if(x < 0 or x >= height or y < 0 or y >= width or
                   i < 0 or i >= height or j < 0 or j >= width):
                    pass
                else:
                    soma += npg_img[i, j][0]
        return float(soma) / (m * n)
    
    def _media_pearson_simplificada(self, npg_img):
        height = npg_img.shape[0]
        width = npg_img.shape[1]

        return self._media_pearson(npg_img, int(height/2), int(width/2), height, width)

    
    def _correlacao_normalizada(self, npg_img, x, y, m, n, media):
        height = npg_img.shape[0]
        width = npg_img.shape[1]

        somaNormal = 0
        soma = 0
        total = float(m*n)
        for i in range(x - int(m/2), x + int(m/2) - self.isPar(m, n) - 1):
            for j in range(y - int(n/2), y + int(n/2) - self.isPar(m, n) - 1):
                if(x < 0 or x >= height or y < 0 or y >= width or
                   i < 0 or i >= height or j < 0 or j >= width):
                    pass
                else:
                    somaNormal += np.abs(media - npg_img[i, j][0])
                    soma += media - npg_img[i, j][0]
            
        soma = soma/total
        somaNormal = somaNormal/total
        return soma / somaNormal

    
    def _correlacao_normalizada_simplificado(self, img, media):
        height = img.shape[0]
        width = img.shape[1]
        
        return self._correlacao_normalizada(img, int(height/2), int(width/2), height, width, media)

    def _destacar_correlacao(self, np_img, px, py, nx, ny, m, n):
        np_img_referencia = np_img.copy()
        for i in range(px - int(m/2), int(m/2) - self.isPar(m, n) + px):
            for j in range(py - int(n/2), int(n/2) - self.isPar(m, n) + py):
                if (((i == px - int(m/2) or i == px + (int(m/2) - self.isPar(m, n) - 1)) or 
                     (j == py - int(n/2) or j == py + (int(n/2) - self.isPar(m, n) - 1))) and
                     (i > 0 and i < np_img.shape[0] and j > 0 and j < np_img.shape[1])):
                    print("i: " + str(i) + " j: " + str(j))
                    np_img_referencia[i, j] = (0, 0, 255)
        
        for i in range(nx - int(m/2), nx + int(m/2) - self.isPar(m, n)):
            for j in range(ny - int(n/2), int(n/2) - self.isPar(m, n) + ny):
                if (((i == nx - int(m/2) or i == nx + (int(m/2) - self.isPar(m, n) - 1)) or 
                     (j == ny - int(n/2) or j == ny + (int(n/2) - self.isPar(m, n) - 1))) and
                     (i > 0 and i < np_img.shape[0] and j > 0 and j < np_img.shape[1])):
                    np_img_referencia[i, j] = (255, 0, 0)

        return np_img_referencia
