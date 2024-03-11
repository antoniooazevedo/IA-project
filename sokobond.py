import pygame as pg
import sys
from scripts.level import Level
import scripts.utils as utils

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

class Game: 
    
    def __init__(self):
        pg.init()
    
        #self.ia = _ 
        self.levelName = "lvl1.txt"
        self.level = None
    
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
            "C": utils.load_image("c-field.png"),
            "up": utils.load_image("con-up.png"),
            "down": utils.load_image("con-down.png"),
            "left": utils.load_image("con-left.png"),
            "right": utils.load_image("con-right.png"),
            "1": utils.load_image("one-con.png"),
            "2": utils.load_image("two-con.png"),
            "3": utils.load_image("three-con.png"),
            "4": utils.load_image("four-con.png")
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
        
        
        self.level = Level(self, self.levelName)        
        self.level.run()

Game().run();