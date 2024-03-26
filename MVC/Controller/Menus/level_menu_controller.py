import pygame as pg 
import sys

from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
from MVC.Model.menu_model import Menu_Model

class Level_Menu_Controller:
    def __init__(self, menu_model: Menu_Model, screen):
        self.model = menu_model
        self.screen = screen
        
        self.playing = False
        
        
    def handle_events(self):
        
        if self.playing:
            self.play_level()
            return True
        else:    
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        self.model.selected = (self.model.selected + 1) % len(self.model.options)
                        return True
                    if event.key == pg.K_UP:
                        self.model.selected = (self.model.selected - 1) % len(self.model.options)
                        return True
                    if event.key == pg.K_RETURN:
                        level = "lvl" + str(self.model.selected + 1) + ".txt"
                        self.create_level(level)
                        self.playing = True
                        return True
                    if event.key == pg.K_ESCAPE:
                        return False
        return True
    
    def create_level(self, level):
        self.level_model = Level_Model(level)
        self.level_view = Level_View(self.level_model, self.screen)
        self.level_controller = Level_Controller(self.level_model)
    
    def play_level(self):
            
        self.level_controller.handle_events()
        
        self.level_view.draw()
        pg.display.update()
        
        self.level_controller.check_win()
        
        if self.level_model.won:
            self.playing = False
            return False
    
        return True