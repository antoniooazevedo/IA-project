import pygame as pg
import sys

from MVC.Model.Entities.molecule_model import Molecule_Model

class Molecule_View:
    def __init__(self, molecule_model: Molecule_Model, screen, path):
        self.model = molecule_model
        self.screen = screen
     
    def draw():
        #go through all the atoms and connections in the molecule model and call their draw methods in their viewer
        pass
       