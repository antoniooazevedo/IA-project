import pygame as pg
import sys
import scripts.utils as utils
from MVC.Model.Entities.wall_model import Wall_Model

class Wall_View:
    def __init__(self, wall_model: Wall_Model, screen, path):
        self.model = wall_model
        self.screen = screen
        self.image = utils.load_image(path)
        
    def draw(self):
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])