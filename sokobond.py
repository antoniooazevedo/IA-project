import pygame as pg
import sys
from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
from MVC.Model.menu_model import Menu_Model
from MVC.View.menu_view import Menu_View
from MVC.Controller.Menus.main_menu_controller import Main_Menu_Controller
from AI.sokobond_state import Sokobond_State
from AI.tree_node import Search, Heuristic
import utils as utils

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

class Game: 
    
    def __init__(self):
        pg.init()
    
        self.levelName = "lvl1.txt"
    
        pg.display.set_caption("Sokobond")
        self.screen = pg.display.set_mode(WINDOW_SIZE)

        self.clock = pg.time.Clock()
        self.fps = 60

    def run(self):
        
        main_menu_model = Menu_Model(["Play", "Choose AI", "Quit"], "SOKOBOND", 50)
        main_menu_view = Menu_View(self.screen, main_menu_model, 1)
        main_menu_controller = Main_Menu_Controller(main_menu_model, self.screen)

        while True:
            main_menu_controller.handle_events()
            
            if (not main_menu_controller.on_level_menu) and (not main_menu_controller.level_menu_controller.playing) and (not main_menu_controller.on_ai_menu):
                main_menu_view.draw()
                pg.display.update()
            
            self.clock.tick(self.fps)

Game().run()