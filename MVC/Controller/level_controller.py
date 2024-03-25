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
        playerMolecule = self.model.get_player_molecule()
        molecule_controller = Molecule_Controller(playerMolecule, self.model.matrix)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_UP:
                    if (molecule_controller.move('up')):
                        atoms = playerMolecule.get_atoms()
                        for atom in atoms:
                            molecule_controller.make_connections(atom)
                elif event.key == pg.K_DOWN:
                    if (molecule_controller.move('down')):
                        atoms = playerMolecule.get_atoms()
                        for atom in atoms:
                            molecule_controller.make_connections(atom)
                elif event.key == pg.K_LEFT:
                    if (molecule_controller.move('left')):
                        atoms = playerMolecule.get_atoms()
                        for atom in atoms:
                            molecule_controller.make_connections(atom)
                elif event.key == pg.K_RIGHT:
                    if (molecule_controller.move('right')):
                        atoms = playerMolecule.get_atoms()
                        for atom in atoms:
                            molecule_controller.make_connections(atom)

    def update(self):
        pass
        
