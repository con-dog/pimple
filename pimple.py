"""
pimple
------
Python IMage Processing Library
"""
from collections import namedtuple
import random
from PIL import Image
import numpy as np


def generate_simple_noise() -> None:
    rng = np.random.default_rng()
    new_pixel_map = rng.integers(256, size=(size.x, size.y, 4))
    for i in range(size.x):
        for j in range(size.y):
            C, M, Y, K = new_pixel_map[i, j]
            pixels[i, j] = (C, M, Y, K)
    image.show()


def generate_complex_noise(step):
    """Accept any given sizings of pixel group"""
    for x in range(0, size.x, step.x):
        for y in range(0, size.y, step.y):
            C, M, Y, K = (random.randint(0, 255) for _ in range(4))  # CHANGE ME
            i = 0
            while (x + i < size.x):
                j = 0
                while (y + j < size.y):
                    pixels[x + i, y + j] = (C, M, Y, K)
                    j += random.randint(1, 3)  # CHANGE ME
                i += random.randint(3, 5)  # CHANGE ME
    image.show()



if __name__ == '__main__':
    mode = 'CMYK'
    Size = namedtuple('Size', ['x', 'y'])
    Step = namedtuple('Step', ['x', 'y'])
    size = Size(500,  500)  # CHANGE ME
    step = Step(20, 20)  # CHANGE ME
    image = Image.new(mode, size)
    pixels = image.load()
    generate_complex_noise(step)
    image.save('examples/white2.JPEG')
