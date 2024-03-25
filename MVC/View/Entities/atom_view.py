import pygame as pg
import sys
import scripts.utils as utils
from MVC.Model.Entities.atom_model import Atom_Model

class Atom_View:
    
    def __init__(self, atom_model: Atom_Model, screen, path, image_electrons):
        self.model = atom_model
        self.screen = screen
        self.image = utils.load_image(path)        
        self.image_electrons = image_electrons
        self.wtf = utils.BASE_IMG_PATH 
        
    def draw(self):
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])
        
        if (self.atom.electrons == 1):
            self.screen.blit(self.image_electrons, [self.model.x * 60 + 130, self.model.y * 60])
        
        
        
        