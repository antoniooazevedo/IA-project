import pygame as pg 
import sys

from MVC.Model.menu_model import Menu_Model

class Menu_View:
    
    def __init__(self, screen, menu_model: Menu_Model):
        self.screen = screen
        self.model = menu_model
        
    def draw_text(self, text, font, size, x, y):
        font = pg.font.Font(None, size)
        text = font.render(text, True, (0, 0, 0))
        self.screen.blit(text, (x, y))
        
    def draw(self):
        self.screen.fill((255,255,255))
        self.draw_text(self.model.bigText, self.model.bigFont, 50, 10, 10)
        
        for i in range(len(self.model.options)):
            self.draw_text(self.model.options[i], self.model.optionsFont, 30, 10, 100 + 30*i)
        
        self.draw_selected()
            
    def draw_selected(self):
        self.draw_text(">", self.model.optionsFont, 30, 8, 100 + 30*self.model.selected)