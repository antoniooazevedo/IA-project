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
        
        Loop = True
        
        while Loop:
            self.player.update()
            self.draw()
 
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        Loop = False
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