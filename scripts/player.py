import pygame as pg
import sys
from scripts.entities import Atom, Wall, Connection
import copy


class Player: 
    def __init__(self, atom, game):
        self.atom = atom
        self.molecule = [self.atom]
        self.game = game

    def make_possible_connections(self, matrix):
        
        for atom in self.molecule:    
            
            if (len(atom.connections) < atom.n_connections):# Check above
                if isinstance(matrix[atom.y - 1][atom.x], Atom) and matrix[atom.y - 1][atom.x] not in self.molecule:
                    connection_up = Connection(self.game, atom.x, atom.y, "up")
                    atom.connections.append(connection_up)
                    
                    connection_down = Connection(self.game, atom.x-1, atom.y, "down")
                    matrix[atom.y - 1][atom.x].connections.append(connection_down)
                    
                    self.molecule.append(matrix[atom.y - 1][atom.x])

                # Check below
                if isinstance(matrix[atom.y + 1][atom.x], Atom) and matrix[atom.y + 1][atom.x] not in self.molecule:
                    
                    connection_down = Connection(self.game, atom.x, atom.y, "down")
                    atom.connections.append(connection_down)
                    
                    connection_up = Connection(self.game, atom.x, atom.y+1, "up")
                    matrix[atom.y + 1][atom.x].connections.append(connection_up)
                    
                    self.molecule.append(matrix[atom.y + 1][atom.x])

                # Check left
                if isinstance(matrix[atom.y][atom.x - 1], Atom) and matrix[atom.y][atom.x - 1] not in self.molecule:
 
                    connection_left = Connection(self.game, atom.x, atom.y, "left")
                    atom.connections.append(connection_left)
                    
                    connection_right = Connection(self.game, atom.x-1, atom.y, "right")
                    matrix[atom.y][atom.x - 1].connections.append(connection_right)
 
                    self.molecule.append(matrix[atom.y][atom.x - 1])

                # Check right
                if isinstance(matrix[atom.y][atom.x + 1], Atom) and matrix[atom.y][atom.x + 1] not in self.molecule:

                    connection_right = Connection(self.game, atom.x, atom.y, "right")
                    atom.connections.append(connection_right)
                    
                    connection_left = Connection(self.game, atom.x+1, atom.y, "left")
                    matrix[atom.y][atom.x + 1].connections.append(connection_left)
                    
                    self.molecule.append(matrix[atom.y][atom.x + 1])


    def move_molecule(self):
        can_move = True
        for atom in self.molecule:
            if not atom.check_move(self.molecule):
                can_move = False
                break
            
        if can_move:
            #print("Matrix:", self.game.level.matrix, "\n")
            for atom in self.molecule:
                atom.update()
    
    def update(self):
        self.move_molecule()
        self.make_possible_connections(self.game.level.matrix)
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
    
    def __str__(self):
        molecule_str = ', '.join([str(atom) for atom in self.molecule])
        return f"Player(Atom: {self.atom}, Molecule: [{molecule_str}])"
            
        