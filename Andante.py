import random
import pygame
from pygame.locals import *
import sys
from utils.bg import get_bg
from game import screen_background
from utils import resourcepath
from utils import essfolder
from game import screen_upbar
from game import maps_container
from utils.game import mapparser

# //////////////////////////////////////////////////////////////////////////////
essfolder.make()
# //////////////////////////////////////////////////////////////////////////////
pygame.init()
icon = pygame.image.load(resourcepath.resource_path("src/icon.png"))
pygame.display.set_icon(icon)
flags = DOUBLEBUF  #| FULLSCREEN
screen = pygame.display.set_mode((1280, 720), flags)
screenx, screeny = screen.get_size()
pygame.display.set_caption("Andante")
clock = pygame.time.Clock()
# //////////////////////////////////////////////////////////////////////////////
LightFont15 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Light.ttf"), int(screeny / 15))
LightFont20 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Light.ttf"), int(screeny / 20))
LightFont25 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Light.ttf"), int(screeny / 25))
LightFont30 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Light.ttf"), int(screeny / 30))
LightFont35 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Light.ttf"), int(screeny / 35))
LightFont40 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Light.ttf"), int(screeny / 40))
RegularFont30 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Regular.ttf"), int(screeny / 30))
BoldFont30 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Bold.ttf"), int(screeny / 30))
BoldFont25 = pygame.font.Font(resourcepath.resource_path("src/fonts/Pretendard-Bold.ttf"), int(screeny / 25))
# //////////////////////////////////////////////////////////////////////////////
bgarray = get_bg.get("src/bg", pygame, screenx, screeny)
bgnum = random.randrange(0, len(bgarray))
maplist = maps_container.get()
# //////////////////////////////////////////////////////////////////////////////
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEWHEEL:
                pass

    dt = clock.tick(60)

    screen.fill((0, 0, 0))

    screen_background.draw(screen, bgarray[bgnum])
    screen_upbar.draw(screen, pygame, screenx, screeny)
    maps_container.draw(screen, pygame, screenx, screeny, maplist, BoldFont25, LightFont40)
    pygame.display.flip()
    #print(clock.get_fps())
# //////////////////////////////////////////////////////////////////////////////
pygame.quit()
sys.exit()
