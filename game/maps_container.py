import glob
import os
from utils import resourcepath


def get():
    target = resourcepath.resource_path(os.path.join("maps", "*andante"))
    clist = glob.glob(target)
    return clist