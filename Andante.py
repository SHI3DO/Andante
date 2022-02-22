import random

import pygame
from pygame.locals import *
import sys
import os
from utils.bg import get_bg
from game import screen_background
from utils import resourcepath

pygame.init()
icon = pygame.image.load(resourcepath.resource_path("src/icon.png"))
pygame.display.set_icon(icon)
flags = DOUBLEBUF  # | FULLSCREEN
screen = pygame.display.set_mode((1280, 720), flags)
screenx, screeny = screen.get_size()
pygame.display.set_caption("Andante")

clock = pygame.time.Clock()

bgarray = get_bg.get("src/bg", pygame, screenx, screeny)
bgnum = random.randrange(0, len(bgarray))
print(bgnum)

mainLoop = True
while mainLoop:
    events = pygame.event.get()

    if events:
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mainLoop = False

    dt = clock.tick(120)
    screen_background.draw(screen, bgarray[bgnum])
    pygame.display.flip()

pygame.quit()
