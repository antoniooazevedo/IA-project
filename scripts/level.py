import sys
import pygame as pg

import scripts.utils as utils
from scripts.entities import Atom
from scripts.player import Player

class Level: 
    def __init__(self, game, level):
        
        self.game = game
        (walls, player, entities) = utils.scrape_level(level, game)
        print("Walls: {} \n Player: {} \n Entities: {}".format(walls, player, entities))
        self.walls = walls
        self.entities = entities
        self.player = Player(player, self.game)
        
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
                    
            self.game.clock.tick(self.game.FPS)