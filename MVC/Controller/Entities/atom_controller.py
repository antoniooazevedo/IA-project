import pygame as pg
import sys
from MVC.Model.Entities.atom_model import AtomModel

class Atom_Controller:
    def __init__(self, atomModel: AtomModel, matrix):
        self.atom = atomModel
        self.matrix = matrix
    
    def move(self, new_x, new_y):
        self.atom.x = new_x
        self.atom.y = new_y

        
