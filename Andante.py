import pygame
from pygame.locals import *
import sys
import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception as e:
        print(e)
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pygame.init()
icon = pygame.image.load(resource_path("src/icon.png"))
pygame.display.set_icon(icon)
screensize = pygame.display.Info()
flags = DOUBLEBUF  # | FULLSCREEN
# screen = pygame.display.set_mode((screensize.current_w, screensize.current_h))
screen = pygame.display.set_mode((1280, 720), flags)
pygame.display.set_caption("Andante")

clock = pygame.time.Clock()

mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mainLoop = False
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    dt = clock.tick(120)

    pygame.display.flip()

pygame.quit()
