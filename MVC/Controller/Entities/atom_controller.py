import pygame as pg
import sys
from MVC.Model.Entities.atom_model import Atom_Model

class Atom_Controller:
    def __init__(self, Atom_Model: Atom_Model, matrix):
        self.atom = Atom_Model
        self.matrix = matrix

    def can_move(self, direction):
        x, y = self.atom.get_position()
        if direction == 'up':
            return y > 0 and self.matrix[y - 1][x] is None
        elif direction == 'down':
            return y < len(self.matrix[0]) - 1 and self.matrix[y + 1][x] is None
        elif direction == 'left':
            return x > 0 and self.matrix[y][x - 1] is None
        elif direction == 'right':
            return x < len(self.matrix[0]) - 1 and self.matrix[y][x + 1] is None
        else:
            raise ValueError('Invalid direction')

    def move(self, direction):
        if self.can_move(direction):
            x, y = self.atom.get_position()
            if direction == 'up':
                self.atom.y -= 1
            elif direction == 'down':
                self.atom.y += 1
            elif direction == 'left':
                self.atom.x -= 1
            elif direction == 'right':
                self.atom.x += 1
            else:
                raise ValueError('Invalid direction')
        else:
            print(f"Cannot move {direction}")
                




        
