import pygame as pg
import sys
from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
import utils as utils

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

class Game: 
    
    def __init__(self):
        pg.init()
    
        #self.ia = _ 
        self.levelName = "lvl2.txt"
    
        pg.display.set_caption("Sokobond")
        self.screen = pg.display.set_mode(WINDOW_SIZE)

        self.clock = pg.time.Clock()
        self.fps = 60;

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
        
        
        self.level_model = Level_Model(self.levelName)
        self.level_view = Level_View(self.level_model, self.screen)
        self.level_controller = Level_Controller(self.level_model)     
        
        
        while (not self.level_controller.check_win()):
            
            self.level_controller.handle_events()
            
            self.level_view.draw()
            pg.display.update()
            
            self.clock.tick(self.fps)
        
        pg.quit()
        sys.exit()

Game().run();