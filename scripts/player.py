import pygame as pg
import sys
from scripts.entities import Atom, Wall


class Player: 
    def __init__(self, atom, game):
        self.atom = atom
        self.game = game
        self.molecule = [self.atom]

    def make_possible_connections(self, matrix):
        for atom in self.molecule:
            if sum(atom.connections) >= atom.n_connections:
                continue  

            # Check above
            if isinstance(matrix[atom.y - 1][atom.x], Atom) and matrix[atom.y - 1][atom.x] not in self.molecule:
                atom.connections[0] = 1
                matrix[atom.y - 1][atom.x].connections[1] = 1
                self.molecule.append(matrix[atom.y - 1][atom.x])

            # Check below
            if isinstance(matrix[atom.y + 1][atom.x], Atom) and matrix[atom.y + 1][atom.x] not in self.molecule:
                atom.connections[1] = 1
                matrix[atom.y + 1][atom.x].connections[0] = 1
                self.molecule.append(matrix[atom.y + 1][atom.x])

            # Check left
            if isinstance(matrix[atom.y][atom.x - 1], Atom) and matrix[atom.y][atom.x - 1] not in self.molecule:
                atom.connections[2] = 1
                matrix[atom.y][atom.x - 1].connections[3] = 1
                self.molecule.append(matrix[atom.y][atom.x - 1])

            # Check right
            if isinstance(matrix[atom.y][atom.x + 1], Atom) and matrix[atom.y][atom.x + 1] not in self.molecule:
                atom.connections[3] = 1
                matrix[atom.y][atom.x + 1].connections[2] = 1
                self.molecule.append(matrix[atom.y][atom.x + 1])


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
        self.make_possible_connections(self.game.level.matrix)
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
            
        