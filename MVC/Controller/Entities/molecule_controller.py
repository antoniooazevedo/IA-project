import pygame as pg
import sys
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Controller.Entities.atom_controller import Atom_Controller
from MVC.Controller.Entities.connection_controller import Connection_Controller

class Molecule_Controller:
    def __init__(self, molecule_Model: Molecule_Model, matrix):
        self.model = molecule_Model
        self.matrix = matrix

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.move('up')
                elif event.key == pg.K_DOWN:
                    self.move('down')
                elif event.key == pg.K_LEFT:
                    self.move('left')
                elif event.key == pg.K_RIGHT:
                    self.move('right')

        