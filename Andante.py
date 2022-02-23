import random

import pygame
from pygame.locals import *
import sys
from utils.bg import get_bg
from game import screen_background
from utils import resourcepath
from utils import essfolder
from game import screen_upbar

essfolder.make()

pygame.init()
icon = pygame.image.load(resourcepath.resource_path("src/icon.png"))
pygame.display.set_icon(icon)
flags = DOUBLEBUF#| FULLSCREEN
screen = pygame.display.set_mode((1280, 720), flags)
screenx, screeny = screen.get_size()
pygame.display.set_caption("Andante")

clock = pygame.time.Clock()

bgarray = get_bg.get("src/bg", pygame, screenx, screeny)
bgnum = random.randrange(0, len(bgarray))

mainLoop = True
while mainLoop:
    events = pygame.event.get()
    if events:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mainLoop = False

    dt = clock.tick(60)

    screen.fill((0, 0, 0))

    screen_background.draw(screen, bgarray[bgnum])
    screen_upbar.draw(screen, pygame, screenx, screeny)
    pygame.display.flip()

pygame.quit()
sys.exit()
