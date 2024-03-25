import pygame as pg
import sys

class Molecule_Model:
    def __init__(self, atoms, connections_list, isPlayer=False):
        
        self.isPlayer = isPlayer
        self.molecule = dict()
        
        for (atom, connections) in zip(atoms, connections_list):
            self.molecule[atom] = connections
            
    
