import pygame as pg
import sys

from MVC.Model.level_model import Level_Model
from MVC.Controller.Entities.molecule_controller import Molecule_Controller
from MVC.Model.Entities.molecule_model import Molecule_Model

class Level_Controller:
    
    def __init__(self, level_model: Level_Model):
        self.model = level_model
        
    def check_win(self):
        
        if (len(self.model.molecules) != 1):
            return False
        
        for atom in self.model.molecules[0].get_atoms():
            if atom.get_electrons() != 0:
                return False
            
        return True

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
                            self.remove_old_molecules()

                elif event.key == pg.K_DOWN:
                    if (molecule_controller.move('down')):
                        atoms = playerMolecule.get_atoms()
                        for atom in atoms:
                            molecule_controller.make_connections(atom)
                            self.remove_old_molecules()

                elif event.key == pg.K_LEFT:
                    if (molecule_controller.move('left')):
                        atoms = playerMolecule.get_atoms()
                        for atom in atoms:
                            molecule_controller.make_connections(atom)
                            self.remove_old_molecules()

                elif event.key == pg.K_RIGHT:
                    if (molecule_controller.move('right')):
                        atoms = playerMolecule.get_atoms()
                        for atom in atoms:
                            molecule_controller.make_connections(atom)
                            self.remove_old_molecules()

    def remove_old_molecules(self):
        self.model.molecules = []
        for x in self.model.matrix:
            for elem in x:
                if (isinstance(elem, Molecule_Model) and elem not in self.model.molecules): 
                    self.model.molecules.append(elem)
        
