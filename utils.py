import pygame as pg

BASE_IMG_PATH = "assets/images/"

def load_image(path):
    """
    Load an image from the assets folder and scale it to 60x60 pixels.
    """
    img = pg.image.load(BASE_IMG_PATH + path).convert()
    img2 = pg.transform.scale(img, (60, 60))
    img2.set_colorkey((255, 255, 255))  # might change to Black
    return img2
