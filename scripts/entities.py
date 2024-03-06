import pygame as pg

class Atom:
    def __init__(self, game, x, y, type, n_connections=1):
        self.game = game
        self.x = x
        self.y = y
        self.type = type
        self.n_connections = n_connections
        self.connections = [0,0,0,0] #up, down, left, right
    
    def update(self):

        new_x = self.x + (self.game.movement[2] + self.game.movement[3])
        new_y = self.y + (self.game.movement[0] + self.game.movement[1])

        self.game.movement = [0, 0, 0, 0]
        
        self.y = new_y
        self.x = new_x  
        

    def render(self, screen):
        screen.blit(self.game.assets['player'], [self.x, self.y])
        
class Wall:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.type = "wall"
        
    def render(self, screen):
        screen.blit(self.game.assets['wall'], [self.x, self.y])
