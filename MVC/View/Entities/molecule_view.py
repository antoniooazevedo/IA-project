import pygame as pg

from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.View.Entities.atom_view import Atom_View
from MVC.View.Entities.connection_view import Connection_View


class Molecule_View:
    """
    Class that represents the view of a Molecule in the MVC pattern.
    
    It is responsible for drawing the molecule on the screen.
    """
    
    def __init__(self, molecule_model: Molecule_Model, screen, assets):
        """
        Initializes a Molecule_View object.
        
        Args:
            molecule_model (Molecule_Model): The model object containing the molecule data.
            screen (pygame.Surface): The surface to render the molecule on.
            assets (dict): The assets used to draw the molecule.
        """
        self.model = molecule_model
        self.screen = screen
        self.assets = assets

    def draw(self):
        """
        Draw the molecule on the screen.
        
        It draws each atom and connection in the molecule.
        """
        for atom in self.model.molecule.keys():
            type = atom.element
            num_electrons = str(atom.electrons)
            if num_electrons == "0":
                Atom_View(atom, self.screen, self.assets[type], None).draw()
            else:
                Atom_View(
                    atom, self.screen, self.assets[type], self.assets[num_electrons]
                ).draw()

            for connection in self.model.molecule[atom]:
                direction = connection.direction
                Connection_View(connection, self.screen, self.assets[direction]).draw()
