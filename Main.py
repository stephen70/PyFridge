import numpy
import pandas
from PIL import Image
import math

class MagnetBlock(object):
    def __init__(self, color, hexcolor, number):
        self.color = color
        self.hexcolor = hexcolor
        self.number = number


blocks = [
    MagnetBlock('Lime','B8E933', 100),
    MagnetBlock('Black', '000000', 200),
    MagnetBlock('White', 'FFFFFF', 100),
    MagnetBlock('Orange', 'A9570D', 100),
    MagnetBlock('Burgundy', '371C04', 100),
    MagnetBlock('Green', '23950F', 100),
    MagnetBlock('Pink', 'B97C72', 100),
    MagnetBlock('Purple', '2C1A2C', 100),
    MagnetBlock('Blue', '4F6A91', 100),
    MagnetBlock('Light Grey', 'F6F6F6', 100),
    MagnetBlock('Dark Grey', '888888', 100),
    MagnetBlock('Brown', '533C34', 100)
]

block_colors = [block.hexcolor for block in blocks]


def color_distance(color1, color2):
    r1 = int(color1[0:2], 16) # red color value
    g1 = int(color1[2:4], 16) # green color value
    b1 = int(color1[4:6], 16) # blue color value
    r2 = int(color2[0:2], 16) # red color value
    g2 = int(color2[2:4], 16) # green color value
    b2 = int(color2[4:6], 16) # blue color value

    distance = math.sqrt(
        (r2 - r1) ** 2 +
        (g2 - g1) ** 2 +
        (b2 - b1) ** 2)

    return distance


img = Image.open("Images/girl_with_a_pearl_earring.jpg")

# first downsize image for efficiency, wont be using a 1920x1080 image
# then map each pixel to its nearest neighbour

for pixel in img:

width, height = img.size

img_small = img.resize((width//6, height//6))
img_small.show()