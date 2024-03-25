import pygame as pg
import sys

class Wall_Model:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__ (self):
        return f"Wall_Model({self.x}, {self.y})"