import pygame as pg
import sys

import utils as utils
from MVC.Model.level_model import Level_Model
from MVC.Model.Entities.atom_model import Atom_Model
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model
from MVC.View.Entities.atom_view import Atom_View
from MVC.View.Entities.molecule_view import Molecule_View
from MVC.View.Entities.wall_view import Wall_View



class Level_View:
    def __init__(self, level_model: Level_Model, screen):
        self.model = level_model
        self.screen = screen
        self.load_assets()
        
    def load_assets(self):
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

    def draw(self):
        self.screen.fill((255, 255, 255))
        for row in self.model.matrix:
            for entity in row:
                if entity is not None:
                    self.draw_entity(entity)

    def draw_entity(self, entity):
        if isinstance(entity, Molecule_Model):
            Molecule_View(entity, self.screen, self.assets).draw()
        elif isinstance(entity, Wall_Model):
            Wall_View(entity, self.screen, self.assets["wall"]).draw()
            
    def draw_end_of_level(self):
        font = pg.font.Font("assets/fonts/RhodiumLibre-Regular.ttf", 50)
        
        text1 = font.render("You won!", True, (0, 0, 0))
        text1_width = text1.get_width()
        text1_height = text1.get_height()
        x1 = (800 - text1_width) // 2  
        y1 = 600 - text1_height * 2 - 50 
        self.screen.blit(text1, (x1, y1))
        
        text2 = font.render("Press Return to go back.", True, (0, 0, 0))
        text2_width = text2.get_width()
        x2 = (800 - text2_width) // 2 
        y2 = 600 - text1_height - 50  
        self.screen.blit(text2, (x2, y2))