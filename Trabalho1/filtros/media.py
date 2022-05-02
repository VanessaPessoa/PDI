class MediaFilter:

    def isPar(self, m, n):
        modulo = (m * n) % 2
        return (1 if modulo == 0 else 0)

    def apply_filter_media(self, np_image_rgb, m, n):
        np_image_rgb_reference = np_image_rgb.copy()
        
        (width, height, *_) = np_image_rgb.shape

        for x in range(0, width):
            for y in range(0, height):
                np_image_rgb_reference[x, y] = self.calculate_media(
                    np_image_rgb, 
                    x,
                    y,
                    m,
                    n,
                    width,
                    height)

        return np_image_rgb_reference


    def calculate_media(self, np_image_rgb, x, y, m, n, width, height):
        somaR = 0
        somaG = 0
        somaB = 0

        for i in range(x - int(m/2), x + int(m/2) - self.isPar(m, n)):
            for j in range(y - int(n/2), y + int(n/2) - self.isPar(m, n)):
                if self.is_pixel_inside_img(i, j, width, height):
                    (R, G, B) = np_image_rgb[i, j]
                    somaR += R
                    somaG += G
                    somaB += B
                
       
        mediaR = somaR / (m*n)
        mediaG = somaG / (m*n)
        mediaB = somaB / (m*n)

        return (mediaR, mediaG, mediaB)

    def is_pixel_inside_img(self, x, y, width, height):
        if x >= 0 and x < width and y >= 0 and y < height:
            return True 
        return False 
