import pygame as pg
import sys
from scripts.level import Level
import scripts.utils as utils

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Global variables


class Game: 
    
    def __init__(self):
        pg.init()
    
        #self.ia = _ 
        self.level = "lvl1.txt"
    
        pg.display.set_caption("Sokobond")
        self.screen = pg.display.set_mode(WINDOW_SIZE)

        self.clock = pg.time.Clock()
        self.fps = 60;
        self.movement = [0, 0, 0, 0]

        self.assets = {
            "h": utils.load_image("h-player.png"),
            "o": utils.load_image("o-player.png"),
            "n": utils.load_image("n-player.png"),
            "c": utils.load_image("c-player.png"),
            "wall": utils.load_image("wall.png"),
            "H": utils.load_image("h-field.png"),
            "O": utils.load_image("o-field.png"),
            "N": utils.load_image("n-field.png"),
            "C": utils.load_image("c-field.png")
        }
        
        self.n_connections = {
            "H": 1,
            "O": 2,
            "N": 3,
            "C": 4,
            "h": 1,
            "o": 2,
            "n": 3,
            "c": 4
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