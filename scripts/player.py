import pygame as pg
import sys


class Player: 
    def __init__(self, atom, game):
        self.atom = atom
        self.game = game
        self.atoms = [self.atom]
        
    def update(self):
        for atom in self.atoms:
            atom.update()
            
        self.game.movement = [0,0,0,0]
    
    def draw(self):
        for atom in self.atoms:
            atom.render(self.game.screen)
    
    def event_handler(self, event):
        if event.key == pg.K_UP:
            self.game.movement[0] = -60
        elif event.key == pg.K_DOWN:
            self.game.movement[1] = 60
        elif event.key == pg.K_LEFT:
            self.game.movement[2] = -60
        elif event.key == pg.K_RIGHT:
            self.game.movement[3] = 60
            
        