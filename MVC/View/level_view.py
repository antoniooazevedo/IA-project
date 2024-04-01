import pygame as pg

import utils as utils
from MVC.Model.level_model import Level_Model
from MVC.Model.Entities.atom_model import Atom_Model
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model
from MVC.View.Entities.atom_view import Atom_View
from MVC.View.Entities.molecule_view import Molecule_View
from MVC.View.Entities.wall_view import Wall_View


class Level_View:
    """
    Class that represents the view of the Level in the MVC pattern.
    
    It is responsible for drawing the level on the screen.
    """
    def __init__(self, level_model: Level_Model, screen):
        """
        Initializes a Level_View object.
        
        Args:
            level_model (Level_Model): The model object containing the level data.
            screen (pygame.Surface): The surface to render the level on.
        """
        self.model = level_model
        self.screen = screen
        self.load_assets()

    def load_assets(self):
        """
        Loads the assets used by the level.
        """
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
            "4": utils.load_image("four-con.png"),
        }

    def draw(self):
        """
        Draw the level on the screen.
        It clears the screen and then draws each entity in the level matrix.
        Finally, it draws the instructions for the AI at the top of the screen.
        """
        self.screen.fill((255, 255, 255))
        for row in self.model.matrix:
            for entity in row:
                if entity is not None:
                    self.draw_entity(entity)
        self.draw_instructions()

    def draw_instructions(self):
        """
        Draw the instructions for the AI at the top of the screen.
        """
        font = pg.font.Font("assets/fonts/RhodiumLibre-Regular.ttf", 20)
        text = font.render("Press R to solve the level using AI.", True, (0, 0, 0))
        text_width = text.get_width()
        x = 10
        y = 5
        self.screen.blit(text, (x, y))

        text = font.render("Press T to get a tip.", True, (0, 0, 0))
        text_width = text.get_width()
        x = (800 - text_width) - 10
        y = 5
        self.screen.blit(text, (x, y))

    def draw_entity(self, entity):
        """
        Check the type of the entity and call the corresponding View class to draw it.
        
        Args:
            entity (Entity): The entity to draw.
        """
        if isinstance(entity, Molecule_Model):
            Molecule_View(entity, self.screen, self.assets).draw()
        elif isinstance(entity, Wall_Model):
            Wall_View(entity, self.screen, self.assets["wall"]).draw()

    def draw_end_of_level_win(self):
        """
        Draw the message displayed when the player wins the level.
        
        The message is displayed in the center of the screen.
        The placement of the text is calculated based on the dimensions of the screen and the text.
        """
        
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

    def draw_end_of_level_lose(self):
        """
        Draw the message displayed when the player loses the level.
        
        The message is displayed in the center of the screen.
        The placement of the text is calculated based on the dimensions of the screen and the text.
        """
        
        font = pg.font.Font("assets/fonts/RhodiumLibre-Regular.ttf", 50)

        text1 = font.render("Couldn't find a solution!",True, (0, 0, 0))
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

    def draw_creating_AI(self):
        """
        Draws the message displayed when the AI is solving the level, so the player knows he has to wait.
        
        The message is displayed in the center of the screen.
        The placement of the text is calculated based on the dimensions of the screen and the text.
        """
        font = pg.font.Font("assets/fonts/RhodiumLibre-Regular.ttf", 50)

        text1 = font.render("Solving using AI...", True, (0, 0, 0))
        text1_width = text1.get_width()
        text1_height = text1.get_height()
        x1 = (800 - text1_width) // 2
        y1 = 600 - text1_height * 2 - 50
        self.screen.blit(text1, (x1, y1))

        text2 = font.render("Please wait.", True, (0, 0, 0))
        text2_width = text2.get_width()
        x2 = (800 - text2_width) // 2
        y2 = 600 - text1_height - 50
        self.screen.blit(text2, (x2, y2))
