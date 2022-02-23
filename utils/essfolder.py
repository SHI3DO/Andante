import os


def make():
    if not os.path.isdir('./maps'):
        os.mkdir('./maps')