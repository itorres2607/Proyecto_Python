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

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Proyecto")
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
return 0


if __name__ == "__main__":
    pygame.init()
    main()