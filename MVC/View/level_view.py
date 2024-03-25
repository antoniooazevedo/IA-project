import pygame as pg
import sys

import scripts.utils as utils
from MVC.Model.level_model import Level_Model


class Level_View:
    def __init__(self, level_model: Level_Model, screen):
        self.model = level_model
        self.screen = screen
        
    def draw(self):
        # Draw all the molecules and walls
        pass