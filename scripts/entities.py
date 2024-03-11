import pygame as pg

class Atom:
    def __init__(self, game, x, y, type):
        self.game = game
        self.x = x
        self.y = y
        self.type = type
        self.n_connections = self.game.n_connections[self.type]
        self.connections = []
    
    def update(self):

        new_x = self.x + (self.game.movement[2] + self.game.movement[3])
        new_y = self.y + (self.game.movement[0] + self.game.movement[1])
        
        self.y = new_y
        self.x = new_x  
        
        for connection in self.connections:
            connection.update() 
        

    def render(self, screen):
        screen.blit(self.game.assets[self.type], [self.x, self.y])
        screen.blit(self.game.assets[str(self.n_connections)], [self.x, self.y])
        
        
class Wall:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.type = "wall"
        
    def render(self, screen):
        screen.blit(self.game.assets['wall'], [self.x, self.y])
        
class Connection:
    def __init__(self, game, x, y, direction):
        self.game = game
        self.x = x
        self.y = y
        self.direction = direction

    def render(self, screen):
        screen.blit(self.game.assets[self.direction], [self.x, self.y])
        
    def update(self):
        
        new_x = self.x + (self.game.movement[2] + self.game.movement[3])
        new_y = self.y + (self.game.movement[0] + self.game.movement[1])
        
        self.y = new_y
        self.x = new_x  