import pygame as pg 
import sys

from MVC.Model.menu_model import Menu_Model

class Menu_View:
    
    def __init__(self, screen, menu_model: Menu_Model):
        self.screen = screen
        self.model = menu_model
        pg.font.init()
        font_path = "assets/fonts/RhodiumLibre-Regular.ttf"
        self.bigFont = pg.font.Font(font_path, 100)
        self.optionFont = pg.font.Font(font_path, self.model.optionsFontSize)

        
    def draw_big_text(self):
        text = self.bigFont.render(self.model.bigText, True, (0, 0, 0))
        text_width = text.get_width()
        self.screen.blit(text, ((800-text_width)/2, 10))
        
    def draw_options(self):
        options_count = len(self.model.options)
        option_height = self.optionFont.get_height()
        total_height = (options_count // 2 + options_count % 2) * option_height
        start_y = (600 - total_height) // 2 + 100  # 100 is the height of the bigText

        for i in range(options_count):
            text = self.optionFont.render(self.model.options[i], True, (0, 0, 0))
            text_width = text.get_width()
            column = i % 2
            row = i // 2
            x = (400 - text_width) // 2 + column * 400
            y = start_y + row * option_height
            self.screen.blit(text, (x, y))

            
    def draw_selected(self):
        options_count = len(self.model.options)
        option_height = self.optionFont.get_height()
        total_height = (options_count // 2 + options_count % 2) * option_height
        start_y = (600 - total_height) // 2 + 100  # 100 is the height of the bigText

        text = self.optionFont.render(">", True, (0, 0, 0))
        text_width = text.get_width()
        column = self.model.selected % 2
        row = self.model.selected // 2
        x = (400 - text_width) // 2 + column * 400 - 100
        y = start_y + row * option_height
        self.screen.blit(text, (x, y))
        
    def draw(self):
        self.screen.fill((255,255,255))
        self.draw_big_text()
        
        for i in range(len(self.model.options)):
            self.draw_options()
        
        self.draw_selected()
            