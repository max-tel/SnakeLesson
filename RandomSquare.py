#!/usr/bin/env python

import pygame
import sys
import time
import random

from pygame.locals import *


#Pygame initial setup

#FPS controls the speed of the game, as the frames per second is the timer
FPS = 15
pygame.init()
fpsClock=pygame.time.Clock()

#Screen Size
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

surface.fill((255,255,255))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 40)


GRIDSIZE=20
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

screen.blit(surface, (0,0))

def draw_box(surf, color, pos):
    r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
    pygame.draw.rect(surf, color, r)


class Apple(object):
    def __init__(self):
        self.position = (0,0)
        self.colour = (255,0,0)
        self.randomize()

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, surf):
        draw_box(surf, self.colour, self.position)


if __name__ == '__main__':
    apple = Apple()
    apple2 = Apple()
    apple3 = Apple()


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    apple.randomize()
                    apple2.randomize()
                    apple3.randomize()



        surface.fill((255,255,255))
        apple.draw(surface)
        apple2.draw(surface)
        apple3.draw(surface)
        screen.blit(surface, (0,0))

        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS)