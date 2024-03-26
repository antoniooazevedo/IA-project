import pygame as pg
import sys
from MVC.Model.Entities.atom_model import Atom_Model
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model

class Atom_Controller:
    def __init__(self, Atom_Model: Atom_Model, matrix):
        self.atom = Atom_Model
        self.matrix = matrix

    def direction_check(self, direction):
        x, y = self.atom.get_position()
        if direction == 'up':
            return self.matrix[y-1][x]
        
        elif direction == 'down':
            return self.matrix[y+1][x]
        
        elif direction == 'left':
            return self.matrix[y][x-1]
            
        elif direction == 'right':
            return self.matrix[y][x+1]

    

    def move(self, direction):
        if direction == 'up':
            self.atom.y -= 1
        elif direction == 'down':
            self.atom.y += 1
        elif direction == 'left':
            self.atom.x -= 1
        elif direction == 'right':
            self.atom.x += 1
