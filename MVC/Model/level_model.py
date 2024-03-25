import sys
import pygame as pg

from MVC.Model.Entities.molecule_model import Molecule_Model as Molecule_Model
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
        
BASE_LVL_PATH = 'assets/levels/' 

class Level_Model:
    def __init__(self, level):
        self.molecules = []
        self.scrape_level(level)
        self.connect_molecules()
        self.movement = [0, 0, 0, 0]
    
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
                        m_line.append(Wall_Model(col, row)) 
                        
                    elif component.isupper():
                        n = n_connections[component] 
                        atom = Atom_Model(col, row, component, n)
                        molecule = Molecule_Model([atom], [])
                        m_line.append(molecule)
                        self.molecules.append(molecule)

                    elif component.islower():
                        n = n_connections[component]
                        atom = Atom_Model(col, row, component, n, True)
                        molecule = Molecule_Model([atom], [], True)
                        m_line.append(molecule)
                        self.molecules.append(molecule)

                    col += 1 
                row += 1 
                matrix.append(m_line)
        
        self.matrix = matrix
    
    def connect_molecules(self):
        
         for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])): 
                
                entity = self.matrix[x][y]
                
                if isinstance(entity, Molecule_Model):
                    
                    #check up
                    #if isinstance(self.matrix[x-1][y], molecule_model):
                    #    molecule = 

                    #check down
                    #if isinstance(self.matrix[x+1][y], molecule_model):
                    
                    #check left
                    #if isinstance(self.matrix[x][y-1], molecule_model):
                    
                    #check right
                    #if isinstance(self.matrix[x][y+1], molecule_model):
                
                    pass