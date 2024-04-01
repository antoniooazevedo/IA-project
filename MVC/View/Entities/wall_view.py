import pygame as pg
import utils as utils
from MVC.Model.Entities.wall_model import Wall_Model


class Wall_View:
    """
    Class that represents the view of a Wall in the MVC pattern.
    
    It is responsible for drawing the wall on the screen.
    """
    
    def __init__(self, wall_model: Wall_Model, screen, image):
        """
        Initializes a Wall_View object.
        
        Args:
            wall_model (Wall_Model): The model object containing the wall data.
            screen (pygame.Surface): The surface to render the wall on.
            image (pygame.Surface): The image to use for the wall.
        """
        self.model = wall_model
        self.screen = screen
        self.image = image

    def draw(self):
        """
        Draw the wall on the screen.
        """
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])
