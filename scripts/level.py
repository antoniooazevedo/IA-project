import sys
import pygame as pg

import scripts.utils as utils
from scripts.entities import Atom, Connection
from scripts.player import Player

class Level: 

    def __init__(self, game, level):
        self.game = game
        (self.matrix, self.player) = utils.scrape_level(level, game)
        
    def run(self):
        
        End_Loop = False
        
        while not End_Loop:
            
            End_Loop = self.check_win()
            End_Loop = False
            self.player.update()
            self.make_possible_connections(self.matrix)
            self.draw()
 
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        End_Loop = True
                    else:
                        self.player.event_handler(event)
                    
            self.game.clock.tick(self.game.fps)

        pg.quit()
        sys.exit()
        
    def make_possible_connections(self, matrix):
        
        for line in matrix:
            
            for atom in line:    
                
                if ((isinstance(atom, Atom)) and (len(atom.connections) < atom.n_connections)):
                    
                    # Check below
                    if isinstance(matrix[atom.y + 1][atom.x], Atom):
                                                
                        below_atom = matrix[atom.y + 1][atom.x]
                        
                        if (len(below_atom.connections) < below_atom.n_connections):
                                                    
                            connection_down = Connection(self.game, atom.x, atom.y, "down")
                            atom.connections.append(connection_down)
                            
                            connection_up = Connection(self.game, atom.x, atom.y+1, "up")
                            below_atom.connections.append(connection_up)

                            self.player.make_connection(atom, below_atom)                            

                    # Check right
                    if isinstance(matrix[atom.y][atom.x + 1], Atom):

                        right_atom = matrix[atom.y][atom.x + 1]
                        
                        if (len(right_atom.connections) < right_atom.n_connections):
                                
                            connection_right = Connection(self.game, atom.x, atom.y, "right")
                            atom.connections.append(connection_right)
                            
                            connection_left = Connection(self.game, atom.x+1, atom.y, "left")
                            right_atom.connections.append(connection_left)
                            
                            self.player.make_connection(atom, right_atom)

    def draw(self):
        self.game.screen.fill((255,255,255))

        for row in self.matrix:
            for element in row:
                if element != None:
                    element.render(self.game.screen)

        pg.display.flip()
    
    def check_win(self):

        for row in self.matrix:
            for element in row:
                if isinstance(element, Atom):
                    if ( len(element.connections) < element.n_connections ):
                        return False
        return True
    
