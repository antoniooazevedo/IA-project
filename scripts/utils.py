import pygame
from scripts.entities import Atom, Wall
from scripts.player import Player

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img2 = pygame.transform.scale(img, (60, 60))
    img2.set_colorkey((255, 255, 255)) # might change to Black 
    return img2

def scrape_level(level, game):
    matrix = []
    player = None

    row = 0
    col = 0

    with open('assets/levels/' + level, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            col = 0
            m_line = []
            components = line.split(',')
            for component in components:
                if component == ' ':
                    m_line.append(None)
                elif component == '#':
                    m_line.append(Wall(game, col, row)) 
                elif component.isupper():
                    m_line.append(Atom(game, col, row, component))
                elif component.islower():
                    player = Atom(game, col, row, component)
                    m_line.append(player)
                col += 1 
            row += 1 
            matrix.append(m_line)

    return (matrix, Player(player, game))