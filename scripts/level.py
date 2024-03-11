import sys
import pygame as pg

import scripts.utils as utils
from scripts.entities import Atom
from scripts.player import Player

class Level: 

    def __init__(self, game, level):
        self.game = game
        (self.matrix, self.player) = utils.scrape_level(level, game)
        
    def run(self):
        
        End_Loop = False
        
        while not End_Loop:
            
            End_Loop = self.check_win()
            self.player.update()
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
                    if ( sum(element.connections) < element.n_connections ):
                        return False
        return True