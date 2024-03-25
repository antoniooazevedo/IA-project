import pygame as pg
import sys

from MVC.Model.level_model import Level_Model
from MVC.Controller.Entities.molecule_controller import Molecule_Controller

class Level_Controller:
    
    def __init__(self, level_model: Level_Model):
        self.model = level_model
        
    def check_win(self):
        
        if (len(self.model.molecules) != 1):
            return False
    
        for atom in self.model.molecules[0].atoms:
            # We will probably need to change this to a more complex condition
            if (atom.electrons != 0):
                return False

    def handle_events(self):
        player_molecule = self.model.get_player_molecule()
        if player_molecule is not None:
            player_molecule_controller = Molecule_Controller(player_molecule, self.model.matrix)
            player_molecule_controller.handle_events()

    def update(self):
        pass
        
