from glob import glob
from os import path

import pygame

from globals import *

sprites = {}
for filename in glob("sprites/*.png"):
    name = path.splitext(path.basename(filename))[0]

    image = pygame.image.load(filename)
    w,h = image.get_size()
    image = pygame.transform.scale(image,(w*SCALE,h*SCALE))

    sprites[name] = image

