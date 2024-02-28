import pygame

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
    img = pygame.load_image(BASE_IMG_PATH + path).covert()
    img.set_colorkey((255, 255, 255)) # might change to Black 


