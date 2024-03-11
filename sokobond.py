import pygame as pg
import sys
from scripts.level import Level
import scripts.utils as utils

# Constants
WIDTH, HEIGHT = 1920, 1080
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Global variables


class Game: 
    
    def __init__(self):
        pg.init()
    
        #self.ia = _ 
        self.level = "lvl1.txt"
    
        pg.display.set_caption("Sokobond")
        self.screen = pg.display.set_mode(WINDOW_SIZE)

        self.clock = pg.time.Clock()

        self.assets = {
            "player-h": utils.load_image("h-player.png"),
            "player-o": utils.load_image("o-player.png"),
            "player-n": utils.load_image("n-player.png"),
            "player-c": utils.load_image("c-player.png"),
            "wall": utils.load_image("wall.png"),
            "atom-h": utils.load_image("h-field.png"),
            "atom-o": utils.load_image("o-field.png"),
            "atom-n": utils.load_image("n-field.png"),
            "atom-c": utils.load_image("c-field.png")
        }
        
        self.n_connections = {
            "H": 1,
            "O": 2,
            "N": 3,
            "C": 4
        } 

    def run(self):
        
        # Menu interface 
        ## Play
        ## Quit
        
        ## Play
        ### Play as human
        ### Choose IA
        
        ### Levels
        #### 192749127491 levels
        #### Back
        
        
        level = Level(self, self.level)
        
        while True:
            level.run()

Game().run();