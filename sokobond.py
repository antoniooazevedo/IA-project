import pygame as pg
import sys
from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
from MVC.Model.menu_model import Menu_Model
from MVC.View.menu_view import Menu_View
from MVC.Controller.Menus.main_menu_controller import Main_Menu_Controller
from AI.sokobond_state import Sokobond_State
from AI.tree_node import TreeNode
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
        self.fps = 60;

    def run(self):
        
        #main_menu_model = Menu_Model(["Play", "Quit"], "arial", "SOKOBOND", "arial")
        #main_menu_view = Menu_View(self.screen, main_menu_model)
        #main_menu_controller = Main_Menu_Controller(main_menu_model, self.screen)
#
        #while True:
        #    main_menu_controller.handle_events()
        #    
        #    main_menu_view.draw()
        #    pg.display.update()
        #    
        #    self.clock.tick(self.fps)

        
        self.level_model = Level_Model(self.levelName)
        self.level_view = Level_View(self.level_model, self.screen)
        self.level_controller = Level_Controller(self.level_model)   
                
        state = Sokobond_State(self.level_model)
        TreeNode.breadth_first_search(state)
#
        goal = TreeNode.breadth_first_search(state)
        TreeNode.print_solution(goal)

        
        while (not self.level_model.won):
            
            self.level_controller.handle_events()
            
            self.level_view.draw()
            pg.display.update()
            
            self.clock.tick(self.fps)
            
            self.level_controller.check_win()
    
        
        pg.quit()
        sys.exit()

Game().run();