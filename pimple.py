"""
pimple
------
Python IMage Processing Library
"""

from collections import namedtuple

from PIL import Image
import numpy as np


def noise() -> None:
    pixels = image.load()
    rng = np.random.default_rng()
    new_pixel_map = rng.integers(256, size=(size.x, size.y, 4))
    for i in range(size.x):
        for j in range(size.y):
            C, M, Y, K = new_pixel_map[i, j]
            pixels[i, j] = (C, M, Y, K)
    image.show()


if __name__ == '__main__':
    Size = namedtuple('Size', ['x', 'y'])
    size = Size(1000,  1000)
    image = Image.new('CMYK', size)
    noise()
