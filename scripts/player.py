import pygame as pg
import sys
from scripts.entities import Atom, Wall, Connection


class Player: 
    def __init__(self, atom, game):
        self.atom = atom
        self.game = game
        self.molecule = [self.atom]

    def move_molecule(self):
        can_move = True
        for atom in self.molecule:
            if not atom.check_move(self.molecule):
                can_move = False
                break
            
        if can_move:
            for atom in self.molecule:
                atom.update()
    
    def update(self):
        self.move_molecule()
        self.game.movement = [0,0,0,0]
    
    def draw(self):
        self.atom.render(self.game.screen)
    
    def event_handler(self, event):
        if event.key == pg.K_UP:
            self.game.movement[0] = -1
        elif event.key == pg.K_DOWN:
            self.game.movement[1] = 1 
        elif event.key == pg.K_LEFT:
            self.game.movement[2] = -1
        elif event.key == pg.K_RIGHT:
            self.game.movement[3] = 1 
            
    def make_connection(self, atom1, atom2):
        if ((self.inMolecule(atom2)) and (not self.inMolecule(atom1))):
            self.molecule.append(atom1)
            for connection in atom1.connections:
                if (not self.inMolecule(atom1.get_connection(connection))):
                    self.molecule.append(atom1.get_connection(connection))
            
        elif ((self.inMolecule(atom1)) and (not self.inMolecule(atom2))):
            self.molecule.append(atom2)
            for connection in atom2.connections:
                if (not self.inMolecule(atom2.get_connection(connection))):
                    self.molecule.append(atom2.get_connection(connection))
            
    def inMolecule(self, atom):
        return atom in self.molecule