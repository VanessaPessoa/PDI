class MedianFilter:

    def isPar(self, m, n):
        modulo = (m * n) % 2
        return (1 if modulo == 0 else 0)

    def apply_filter_median(self, np_image_yiq, m, n):
        np_image_yiq_reference = np_image_yiq.copy()
        
        (width, height, *_) = np_image_yiq.shape

        for x in range(0, width):
            for y in range(0, height):
                np_image_yiq_reference[x, y] = self.calculate_median_y(
                    np_image_yiq, 
                    x,
                    y,
                    m,
                    n,
                    width,
                    height)

        return np_image_yiq_reference


    def calculate_median_y(self, np_image_yiq, x, y, m, n, width, height):
        valuesY = []
        
        for i in range(x - int(m/2), x + int(m/2) - self.isPar(m, n)):
            for j in range(y - int(n/2), y + int(n/2) - self.isPar(m, n)):
                if self.is_pixel_inside_img(i, j, width, height):
                    (Y, I, Q) = np_image_yiq[i, j]
                    valuesY.append(Y)
                else:
                    valuesY.append(0)
        (_, I, Q) = np_image_yiq[x, y]
        
        half = len(valuesY) // 2
        valuesY.sort()
        if not len(valuesY) % 2:
            medianY = (valuesY[half - 1] + valuesY[half]) / 2.0
        medianY = valuesY[half]

        return (medianY, I, Q)

    def is_pixel_inside_img(self, x, y, width, height):
        if x >= 0 and x < width and y >= 0 and y < height:
            return True 
        return False 
