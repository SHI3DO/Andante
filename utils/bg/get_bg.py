import glob
import os
from utils import resourcepath


def get(path, pg, screenx, screeny):
    array = []
    target = resourcepath.resource_path(os.path.join(path, "*png"))
    clist = glob.glob(target)

    for bgimage in clist:
        image = pg.image.load(bgimage).convert_alpha()
        image = pg.transform.smoothscale(image, (screenx, screeny))
        array.append(image)

    return array
