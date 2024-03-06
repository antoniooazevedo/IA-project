import pygame as pg
import sys

from scripts.entities import Atom

class Player: 
    def __init__(self, atom, game):
        self.atom = atom
        self.game = game
        self.atoms = [self.atom]
        
    def update(self):
        for atom in self.atoms:
            atom.update()
    
    def draw(self):
        for atom in self.atoms:
            atom.render(self.game.screen)
    
    def event_handler(self, event):
        if event.key == pg.K_UP:
            self.game.movement[0] = -self.game.block_size
        elif event.key == pg.K_DOWN:
            self.game.movement[1] = self.game.block_size
        elif event.key == pg.K_LEFT:
            self.game.movement[2] = -self.game.block_size
        elif event.key == pg.K_RIGHT:
            self.game.movement[3] = self.game.block_size
            
        