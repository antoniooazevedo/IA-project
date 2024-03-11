import pygame as pg

class Atom:
    def __init__(self, game, x, y, type):
        self.game = game
        self.x = x
        self.y = y
        self.type = type
        self.n_connections = self.game.n_connections[self.type]
        self.connections = [0,0,0,0] #up, down, left, right
        
    
    def update(self):

        new_x = self.x + (self.game.movement[2] + self.game.movement[3])
        new_y = self.y + (self.game.movement[0] + self.game.movement[1])

        self.game.movement = [0, 0, 0, 0]
        
        self.y = new_y
        self.x = new_x  
        

    def render(self, screen):
        screen.blit(self.game.assets[self.type], [self.x * 60 + 130, self.y * 60])
        
class Wall:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.type = "wall"
        
    def render(self, screen):
        screen.blit(self.game.assets['wall'], [self.x * 60 + 130, self.y * 60])
