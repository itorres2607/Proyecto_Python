# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorKey(color, RLEACCEL)

return image


