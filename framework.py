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


screen.blit(surface, (0,0))

if __name__ == '__main__':
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:



        surface.fill((255,255,255))
        screen.blit(surface, (0,0))

        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS)