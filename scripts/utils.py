import pygame

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((255, 255, 255)) # might change to Black 
    return img


