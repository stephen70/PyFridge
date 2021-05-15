import numpy
import pandas
from PIL import Image
import math
import itertools

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

def rgb_to_hex(rgb):
    hex = f'{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
    return hex

def hex_to_rgb(hex):
    r = int(hex[0:2], 16) # red color value
    g = int(hex[2:4], 16) # green color value
    b = int(hex[4:6], 16) # blue color value
    return (r, g, b)

def color_distance(color1, color2):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)

    # no need to take square root, for efficiency

    distance = (r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2
    return distance

img = Image.open("Images/girl_with_a_pearl_earring.jpg")

# first downsize image for efficiency, wont be using a 1920x1080 image
# then map each pixel to its nearest neighbour
img_small = img.resize((100, 100))

width, height = img_small.size

for pixel in itertools.product(range(width), range(height)):
    print(pixel)
    rgb = img_small.getpixel(xy=(pixel))
    hex = rgb_to_hex(rgb)

    distances = [(color_distance(hex, block_color), block_color) for block_color in block_colors]
    distances = sorted(distances, key=lambda x: x[0])
    new_color_hex = distances[0][1]
    new_color_rgb = hex_to_rgb(new_color_hex)

    img_small.putpixel(xy=(pixel), value=new_color_rgb)

img_small.show()