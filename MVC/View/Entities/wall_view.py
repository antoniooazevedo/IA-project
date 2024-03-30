import pygame as pg
import utils as utils
from MVC.Model.Entities.wall_model import Wall_Model


class Wall_View:
    def __init__(self, wall_model: Wall_Model, screen, image):
        self.model = wall_model
        self.screen = screen
        self.image = image

    def draw(self):
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])
