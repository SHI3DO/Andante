import pygame


pygame.init()
screensize = pygame.display.Info()
screen = pygame.display.set_mode((screensize.current_w, screensize.current_h))
pygame.display.set_caption("Andante")