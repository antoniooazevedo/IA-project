import sys
import pygame as pg

from MVC.Model.Entities.molecule_model import Molecule_Model as Molecule_Model
from MVC.Controller.Entities.molecule_controller import Molecule_Controller 
from MVC.Model.Entities.atom_model import Atom_Model as Atom_Model
from MVC.Model.Entities.wall_model import Wall_Model as Wall_Model
from MVC.Model.Entities.connection_model import Connection_Model as Connection_Model

n_connections = {
        "H": 1,
        "O": 2,
        "N": 3,
        "C": 4,
        "h": 1,
        "o": 2,
        "n": 3,
        "c": 4
        }

image_paths = {
    "H": 'assets/images/h-field.png',
    "O": 'assets/images/o-field.png',
    "N": 'assets/images/n-field.png',
    "C": 'assets/images/c-field.png',
    "h": 'assets/images/h-player.png',
    "o": 'assets/images/o-player.png',
    "n": 'assets/images/n-player.png',
    "c": 'assets/images/c-player.png',
    "#": 'assets/images/wall.png'
}
        
BASE_LVL_PATH = 'assets/levels/' 

class Level_Model:
    def __init__(self, level):
        self.molecules = []
        self.scrape_level(level)
    
    def scrape_level(self, level):

        matrix = []
        
        row= 0
        col = 0
        
        with open(BASE_LVL_PATH + level, 'r') as file:
            lines = file.read().split('\n')
            for line in lines:
                col = 0
                m_line = []
                components = line.split(',')
                for component in components:
                    if component == ' ':
                        m_line.append(None)

                    elif component == '#':
                        m_line.append(Wall_Model(col, row, image_paths[component])) 
                        
                    elif component.isupper():
                        n = n_connections[component] 
                        atom = Atom_Model(col, row, component, n, False, image_paths[component])
                        molecule = Molecule_Model([atom], [])
                        
                        m_line.append(molecule)
                        self.molecules.append(molecule)

                    elif component.islower():
                        n = n_connections[component]
                        atom = Atom_Model(col, row, component, n, True, image_paths[component])
                        molecule = Molecule_Model([atom], [], True)
                        m_line.append(molecule)
                        self.molecules.append(molecule)

                    col += 1 
                row += 1 
                matrix.append(m_line)
        
        self.matrix = matrix

    def get_player_molecule(self):
        for molecule in self.molecules:
            if molecule.isPlayer:
                return molecule
        return None
    
                    