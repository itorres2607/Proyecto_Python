# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

#classes
#-----------------------------------------------------------------------

class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5,-0.5]

    def actualizar(self , time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = - self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = - self.speed[1]
            self.rect.centery += self.speed[1] * time



class ladrillo(pygame.sprite.Sprite):
    def __init__(self , x ):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5

    def mover(self , time , keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time




#------------------------------------------------------------------------





#functions
#-----------------------------------------------------------------------------------

def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)

    return image


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Proyecto")

    background_image = load_image('imagenes/fondo_pong.png')
    bola = ball()
    p1 = ladrillo(30)

    clock = pygame.time.Clock()



    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        bola.actualizar(time)
        p1.mover(time , keys)
        screen.blit(background_image, (0,0))
        screen.blit(bola.image, bola.rect)
        screen.blit(p1.image , p1.rect)
        pygame.display.flip()

    return 0

#---------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    pygame.init()
    main()

