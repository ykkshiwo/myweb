"""
from PIL import Image


class Hua:
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    def __init__(self, img_file, width, height):
        self.IMG = img_file
        self.WIDTH = width
        self.HEIGHT = height

    def get_char(self, r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        length = len(self.ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1) / length
        return self.ascii_char[int(gray / unit)]

    def hua(self):
        im = Image.open(self.IMG)
        im = im.resize((self.WIDTH, self.HEIGHT), Image.NEAREST)
        txt = ""
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                txt += self.get_char(*im.getpixel((j, i)))
            txt += '\n'
        '''if self.OUTPUT:
            with open(self.OUTPUT + "/outputok.txt", 'w') as f:
                f.write(txt)'''
        return txt
                """