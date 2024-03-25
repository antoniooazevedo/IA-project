import pygame as pg
import sys
from MVC.Model.Entities.atom_model import Atom_Model
from MVC.Model.Entities.wall_model import Wall_Model

class Atom_Controller:
    def __init__(self, Atom_Model: Atom_Model, matrix):
        self.atom = Atom_Model
        self.matrix = matrix

    def can_move(self, direction):
        x, y = self.atom.get_position()
        if direction == 'up':
            if isinstance(self.matrix[y - 1][x],Wall_Model):
                return False
            #elif isinstance(self.matrix[y - 1][x],Atom_Model):
            #    return self.matrix[y - 1][x].can_move(direction)
            else:
                return True
        
        elif direction == 'down':
            if isinstance(self.matrix[y + 1][x],Wall_Model):
                return False
            #elif isinstance(self.matrix[y + 1][x],Atom_Model):
            #    return self.matrix[y + 1][x].can_move(direction)
            else:
                return True    
        
        
        elif direction == 'left':
            if isinstance(self.matrix[y][x - 1],Wall_Model):
                return False
            #elif isinstance(self.matrix[y][x - 1],Atom_Model):
            #    return self.matrix[y][x - 1].can_move(direction)
            else:
                return True
            
        elif direction == 'right':
            if isinstance(self.matrix[y][x + 1],Wall_Model):
                return False
            #elif isinstance(self.matrix[y][x + 1],Atom_Model):
            #    return self.matrix[y][x + 1].can_move(direction)
            else:
                return True
                
        return False
    
    

    def move(self, direction):
        if self.can_move(direction):
            if direction == 'up':
                self.atom.y -= 1
                return True
            elif direction == 'down':
                self.atom.y += 1
                return True
            elif direction == 'left':
                self.atom.x -= 1
                return True
            elif direction == 'right':
                self.atom.x += 1
                return True
        return False  




        
