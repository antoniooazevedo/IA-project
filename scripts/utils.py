import pygame
from scripts.entities import Atom, Wall

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img2 = pygame.transform.scale(img, (60, 60))
    img2.set_colorkey((255, 255, 255)) # might change to Black 
    return img2

def scrape_level(level, game):
    walls = []
    entities = []
    player = None

    x = 0
    y = 0

    with open('assets/levels/' + level, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            x = 0
            components = line.split(',')
            for component in components:
                if component == ' ':
                    x += 60
                    continue
                elif component == '#':
                    walls.append(Wall(game, x, y))
                elif component.isupper():
                    entities.append(Atom(game, x, y, component))
                elif component.islower():
                    player = Atom(game, x, y, component)
                    entities.append(player)
                x += 60
            y += 60

    return (walls, player, entities)
