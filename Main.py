import colormath
import numpy
import pandas
from PIL import Image
import math
import itertools
import copy

from colormath import color_objects
from colormath import color_diff
from colormath import color_conversions

class MagnetBlock(object):
    def __init__(self, color, hexcolor, number):
        self.color = color
        self.hexcolor = hexcolor
        self.number = number


blocks = [
    MagnetBlock('Lime','C2F636', 100),
    MagnetBlock('Black', '000000', 200),
    MagnetBlock('White', 'FFFFFF', 100),
    MagnetBlock('Orange', 'A9570D', 100),
    MagnetBlock('Burgundy', '371C04', 100),
    MagnetBlock('Light Green', 'AAD82C', 100),
    MagnetBlock('Green', '23950F', 100),
    MagnetBlock('Salmon', 'FF9696', 100),
    MagnetBlock('Purple', '2C1A2C', 100),
    MagnetBlock('Turquoise', 'ACEBDD', 100),
    MagnetBlock('Light Blue', '4F6A91', 100),
    MagnetBlock('Dark Blue', '315992', 100),
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

def color_distance(hex1, hex2):
    rgb1 = color_objects.sRGBColor.new_from_rgb_hex(f"#{hex1}")
    rgb2 = color_objects.sRGBColor.new_from_rgb_hex(f"#{hex2}")

    lab1 = color_conversions.convert_color(rgb1, color_objects.LabColor)
    lab2 = color_conversions.convert_color(rgb2, color_objects.LabColor)

    distance = int(color_diff.delta_e_cie1994(lab1, lab2))
    return distance


def test_size(test_image):
    width, height = test_image.size
    test_blocks = copy.deepcopy(blocks)

    for pixel in itertools.product(range(width), range(height)):
        rgb = test_image.getpixel(xy=pixel)
        if original_img.format == "PNG" and rgb[-1] == 0:
            # skip if transparent pixel
            continue
        hex = rgb_to_hex(rgb[:3])

        replacement_block = min(test_blocks, key=lambda x: color_distance(hex, x.hexcolor))

        if replacement_block.number == 0:
            print(f"Out of color {replacement_block.color}!")
            return False
        else:
            replacement_block.number -= 1
            new_color_rgb = hex_to_rgb(replacement_block.hexcolor)
            test_image.putpixel(xy=(pixel), value=new_color_rgb)

    return True

original_img = Image.open("Images/starry_starry_night.jpg")
original_width, original_height = original_img.size
img_ratio = original_width / original_height

width, height = (10 * img_ratio), 10
previous_img = original_img.resize((int(width), height))
while True:
    # best resample methods are Nearest and Hamming, to preserve blockiness and stop colors being mushed together
    test_img = original_img.resize((int(width), height), resample=Image.NEAREST)
    print(f"Testing width {int(width)} and height {height}...")
    fit_successful = test_size(test_img)
    if fit_successful:
        height += 2
        width += 2 * img_ratio
        previous_img = test_img
    else:
        finished_img = previous_img
        break

finished_img.show()
a = 1