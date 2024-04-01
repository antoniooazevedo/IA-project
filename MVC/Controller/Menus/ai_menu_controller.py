import pygame as pg
import sys

from MVC.Model.menu_model import Menu_Model


class AI_Menu_Controller:
    """
    Class that represents the controller of the AI menu in the MVC pattern.
    
    It is responsible for handling the events of the AI menu, such as the player's movements.
    It also checks if the player has selected an AI.
    """
    
    def __init__(self, menu_model: Menu_Model):
        """
        Initializes an AI_Menu_Controller object.
        Sets the default AI to "A* - Manhattan Distance".
        
        Args:
            menu_model (Menu_Model): The model of the AI menu.
        """
        self.model = menu_model
        self.ai = "A* - Manhattan Distance"

    def handle_events(self):
        """
        Handles the events of the AI menu.
        
        The player can navigate through the AI menu using the arrow keys.
        If the player presses the enter key, the selected AI is stored.
        If the player presses the escape key, the player goes back to the main menu.
        
        Returns:
            bool: True if the player is still in the AI menu, False otherwise.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.model.selected = (self.model.selected - 1) % len(
                        self.model.options
                    )
                    return True
                if event.key == pg.K_RIGHT:
                    self.model.selected = (self.model.selected + 1) % len(
                        self.model.options
                    )
                    return True
                if event.key == pg.K_UP:
                    self.model.selected = (self.model.selected - 1) % len(
                        self.model.options
                    )
                    return True
                if event.key == pg.K_DOWN:
                    self.model.selected = (self.model.selected + 1) % len(
                        self.model.options
                    )
                    return True
                if event.key == pg.K_RETURN:
                    self.select_ia()
                    return False
                if event.key == pg.K_ESCAPE:
                    return False
        return True

    def select_ia(self):
        """
        Selects the AI that the player has chosen.
        """
        
        if self.model.selected == 0:
            self.ai = "BFS"
        elif self.model.selected == 1:
            self.ai = "DFS"
        elif self.model.selected == 2:
            self.ai = "Depth Limited"
        elif self.model.selected == 3:
            self.ai = "Iterative Deepening"
        elif self.model.selected == 4:
            self.ai = "Greedy - Manhattan Distance"
        elif self.model.selected == 5:
            self.ai = "Greedy - Prioritize Free Electrons"
        elif self.model.selected == 6:
            self.ai = "Greedy - Minimize Free Electrons"
        elif self.model.selected == 7:
            self.ai = "A* - Manhattan Distance"
        elif self.model.selected == 8:
            self.ai = "A* - Prioritize Free Electrons"
        elif self.model.selected == 9:
            self.ai = "A* - Minimize Free Electrons"
        elif self.model.selected == 10:
            return
