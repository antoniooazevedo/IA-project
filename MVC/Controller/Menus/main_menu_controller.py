import pygame as pg 
import sys

from MVC.Model.menu_model import Menu_Model
from MVC.View.menu_view import Menu_View
from MVC.Controller.Menus.level_menu_controller import Level_Menu_Controller
from MVC.Controller.Menus.ai_menu_controller import AI_Menu_Controller

class Main_Menu_Controller:
    
    def __init__(self, menu_model: Menu_Model, screen):
        self.model = menu_model
        self.screen = screen
        
        self.ai_type = "Greedy - Manhattan Distance"
        
        self.on_level_menu = False
        self.on_ai_menu = False
        
        self.level_menu_model = Menu_Model(["Level 1","Level 2","Level 3","Level 4","Level 5","Level 6","Level 7","Level 8"], "Choose a level", 50)
        self.level_menu_view = Menu_View(self.screen, self.level_menu_model, 2)
        self.level_menu_controller = Level_Menu_Controller(self.level_menu_model, self.screen, self.ai_type)
        
        self.ai_menu_model = Menu_Model(["BFS","DFS","Depth Limited","Iterative Deepening","Greedy - Manhattan Distance", "Greedy - Free Electrons","Greedy - Still to Implement" ,"A* - Manhattan Distance","A* - Free Electrons","A* - Still to Implement","Back"], "Choose an AI", 25)
        self.ai_menu_view = Menu_View(self.screen, self.ai_menu_model, 2)
        self.ai_menu_controller = AI_Menu_Controller(self.ai_menu_model)
        
    def handle_events(self):
        
        if self.on_level_menu or self.on_ai_menu:
            self.other_menus()
        
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
                            self.level_menu_controller = Level_Menu_Controller(self.level_menu_model, self.screen, self.ai_type)
                            self.on_level_menu = True 
                        if self.model.selected == 1:
                            self.on_ai_menu = True
                        if self.model.selected == 2:
                            pg.quit()
                            sys.exit()
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
        
    def other_menus(self):
        
        if self.on_level_menu:
            if self.level_menu_controller.handle_events():
                if not self.level_menu_controller.playing:
                    self.level_menu_view.draw()
                    pg.display.update()  
            else:
                self.on_level_menu = False
                self.handle_events()
                
        elif self.on_ai_menu:
            if (self.ai_menu_controller.handle_events()):
                self.ai_menu_view.draw()
                pg.display.update()
            else:
                self.on_ai_menu = False
                self.ai_type = self.ai_menu_controller.ai
                self.handle_events()
    