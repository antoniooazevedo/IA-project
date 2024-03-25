import pygame as pg
import sys
from MVC.Model.Entities.atom_model import Atom_Model

class Atom_Controller:
    def __init__(self, Atom_Model: Atom_Model, matrix):
        self.atom = Atom_Model
        self.matrix = matrix

        
