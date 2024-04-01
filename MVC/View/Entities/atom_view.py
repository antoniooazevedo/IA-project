import pygame as pg
import utils as utils
from MVC.Model.Entities.atom_model import Atom_Model

class Atom_View:
    """
    Class that represents the view of an Atom in the MVC pattern.
    
    It is responsible for drawing the atom on the screen.
    """

    def __init__(self, atom_model: Atom_Model, screen, image_atom, image_electrons):
        """
        Initializes an Atom_View object.
        
        Args:
            atom_model (Atom_Model): The model object containing the atom data.
            screen (pygame.Surface): The surface to render the atom on.
            image_atom (pygame.Surface): The image to use for the atom.
            image_electrons (pygame.Surface): The image to use for the electrons.
        """
        self.model = atom_model
        self.screen = screen
        self.image = image_atom        
        self.image_electrons = image_electrons
        
    def draw(self):
        """
        Draw the atom on the screen.
        if the atom has electrons, draw them as well.
        """
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])
        if (self.model.electrons > 0):
            self.screen.blit(self.image_electrons, [self.model.x * 60 + 130, self.model.y * 60])
        
        
        
        