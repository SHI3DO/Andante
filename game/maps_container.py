import glob
import os
from utils import resourcepath


def get():
    target = os.path.join("maps/**", "*json")
    clist = glob.glob(target)
    return clist


def draw(screen, pg, screenx, screeny, maplist):
    for mapnum in range(0, len(maplist)):
        upbar = pg.Surface((screenx / 2.3, screeny / 6))
        upbar.set_alpha(120 * (1/(mapnum+1)**0.4))
        upbar.fill((0, 0, 0))
        screen.blit(upbar, (1 + screenx - screenx / 2.3, screeny / 8 + (screeny/98 + screeny / 6)*mapnum))
