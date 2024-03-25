import pygame as pg
import sys
import scripts.utils as utils
from MVC.Model.Entities.connection_model import Connection_Model

class Connection_View:
    def __init__(self, connection_model: Connection_Model, screen, image):
        self.model = connection_model
        self.screen = screen
        self.image = image
        
    def draw(self):
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])      
