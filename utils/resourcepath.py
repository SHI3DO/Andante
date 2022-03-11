import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # PyInstaller creates a temp folder and stores path in _MEIPASS
    except Exception as e:
        print(e)
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)