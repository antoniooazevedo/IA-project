import pygame as pg
import sys
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Controller.Entities.atom_controller import Atom_Controller
from MVC.Controller.Entities.connection_controller import Connection_Controller

class Molecule_Controller:
    def __init__(self, molecule_Model: Molecule_Model, matrix):
        self.model = molecule_Model
        self.matrix = matrix

    def move(self, direction):
        atomController = Atom_Controller(self.model.get_atom(), self.matrix)
        if direction == 'up':
            atomController.move('up')
        elif direction == 'down':
            atomController.move('down')
        elif direction == 'left':
            atomController.move('left')
        elif direction == 'right':
            atomController.move('right')
        else:
            raise ValueError('Invalid direction')
        


    
        