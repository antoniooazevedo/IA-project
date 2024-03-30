import pygame as pg
import utils as utils
from MVC.Model.Entities.atom_model import Atom_Model

class Atom_View:
    
    def __init__(self, atom_model: Atom_Model, screen, image_atom, image_electrons):
        self.model = atom_model
        self.screen = screen
        self.image = image_atom        
        self.image_electrons = image_electrons
        
    def draw(self):
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])
        if (self.model.electrons > 0):
            self.screen.blit(self.image_electrons, [self.model.x * 60 + 130, self.model.y * 60])
        
        
        
        