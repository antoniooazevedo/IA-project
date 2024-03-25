import pygame as pg
import sys

class Connection_Model:
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def __str__ (self):
        if self.direction == 'up' or self.direction == 'down':
            return '|'
        
        elif self.direction == 'left' or self.direction == 'right':
            return '-'

    
                 
        