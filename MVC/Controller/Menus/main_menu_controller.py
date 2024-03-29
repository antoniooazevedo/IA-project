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
        
        self.level_menu_model = Menu_Model(["Level 1","Level 2","Level 3","Level 4","Level 5","Level 6","Level 7","Level 8"], "Choose a level", 50)
        self.level_menu_view = Menu_View(self.screen, self.level_menu_model, 2)
        self.level_menu_controller = Level_Menu_Controller(self.level_menu_model, self.screen, "Player")
        
    def handle_events(self):
        
        if self.on_level_menu:
            self.level_menu()
        
        else:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.model.selected = (self.model.selected + 1) % len(self.model.options)
                    if event.key == pg.K_LEFT:
                        self.model.selected = (self.model.selected - 1) % len(self.model.options)
                    if event.key == pg.K_UP:
                        self.model.selected = (self.model.selected - 1) % len(self.model.options)
                    if event.key == pg.K_DOWN:
                        self.model.selected = (self.model.selected + 1) % len(self.model.options)
                    
                    
                    if event.key == pg.K_RETURN:
                        if self.model.selected == 0:
                            self.level_menu_controller = Level_Menu_Controller(self.level_menu_model, self.screen, "Player")
                            self.on_level_menu = True 
                        if self.model.selected == 1:
                            self.level_menu_controller = Level_Menu_Controller(self.level_menu_model, self.screen, "AI")
                            self.on_level_menu = True
                        if self.model.selected == 2:
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