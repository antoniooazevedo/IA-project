import pygame as pg
import sys

class Atom_Model:
    
    def __init__(self, x, y, element, electrons, isPlayer=False, image_path=""):
        self.x = x
        self.y = y
        self.element = element
        self.electrons = electrons
        self.isPlayer = isPlayer
        self.image_path = image_path
    
    def __str__(self):
        return self.element
    

