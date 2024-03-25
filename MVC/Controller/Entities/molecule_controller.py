import pygame as pg
import sys
from MVC.Model.Entities.molecule_model import MoleculeModel

class MoleculeController:
    def __init__(self, moleculeModel: MoleculeModel, matrix):
        self.model = moleculeModel
        self.matrix = matrix