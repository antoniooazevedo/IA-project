import pygame as pg
import sys

class Connection_Model:
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def __str__ (self):
        return f'Connection_Model: x={self.x}, y={self.y}, direction={self.direction}'
                 
        