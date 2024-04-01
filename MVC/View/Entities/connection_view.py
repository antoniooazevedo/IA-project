import pygame as pg
import utils as utils
from MVC.Model.Entities.connection_model import Connection_Model


class Connection_View:
    """
    Class that represents the view of a Connection in the MVC pattern.
    
    It is responsible for drawing the connection on the screen.
    """
    
    def __init__(self, connection_model: Connection_Model, screen, image):
        """
        Initializes a Connection_View object.
        
        Args:
            connection_model (Connection_Model): The model object containing the connection data.
            screen (pygame.Surface): The surface to render the connection on.
            image (pygame.Surface): The image to use for the connection.
        """
        self.model = connection_model
        self.screen = screen
        self.image = image

    def draw(self):
        self.screen.blit(self.image, [self.model.x * 60 + 130, self.model.y * 60])
