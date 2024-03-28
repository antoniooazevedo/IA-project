import pygame as pg 
import sys

from MVC.Model.menu_model import Menu_Model
from MVC.View.menu_view import Menu_View
from MVC.Controller.Menus.level_menu_controller import Level_Menu_Controller

class Main_Menu_Controller:
    
    def __init__(self, menu_model: Menu_Model, screen):
        self.model = menu_model
        self.screen = screen
        
        self.on_level_menu = False
        
        self.level_menu_model = Menu_Model(["lvl1", "lvl2", "lvl3"], "arial", "Choose a level", "arial")
        self.level_menu_view = Menu_View(self.screen, self.level_menu_model)
        self.level_menu_controller = Level_Menu_Controller(self.level_menu_model, self.screen)
        
    def handle_events(self):
        
        if self.on_level_menu:
            self.level_menu()
        
        else:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        self.model.selected = (self.model.selected + 1) % len(self.model.options)
                    if event.key == pg.K_UP:
                        self.model.selected = (self.model.selected - 1) % len(self.model.options)
                    if event.key == pg.K_RETURN:
                        if self.model.selected == 0:
                            self.on_level_menu = True 
                        if self.model.selected == 1:
                            pg.quit()
                            sys.exit()
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
        
    def level_menu(self):
        
        if self.level_menu_controller.handle_events():
            if not self.level_menu_controller.playing:
                self.level_menu_view.draw()
                pg.display.update()                
        else:
            self.on_level_menu = False
            self.handle_events()