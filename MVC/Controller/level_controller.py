import pygame as pg
import sys

from MVC.Model.level_model import Level_Model

class Level_Controller:
    
    def __init__(self, level_model: Level_Model):
        self.model = level_model
        
    def check_win(self):
        
        if (len(self.model.molecules) != 1):
            return False
    
        for atom in self.model.molecules[0].atoms:
            # We will probably need to change this to a more complex condition
            if (atom.electrons != 0):
                return False

    def handle_events(self):
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_UP:
                    self.model.movement[0] = -1
                elif event.key == pg.K_DOWN:
                    self.model.movement[1] = 1 
                elif event.key == pg.K_LEFT:
                    self.model.movement[2] = -1
                elif event.key == pg.K_RIGHT:
                    self.model.movement[3] = 1 
        
    def update(self):
        pass
        
