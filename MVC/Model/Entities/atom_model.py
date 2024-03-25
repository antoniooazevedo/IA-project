import pygame as pg
import sys

class Atom_Model:
    
    def __init__(self, x, y, element, electrons, isPlayer=False):
        self.x = x
        self.y = y
        self.element = element
        self.electrons = electrons
        self.isPlayer = isPlayer
    
    def __str__(self):
        return self.element
    

