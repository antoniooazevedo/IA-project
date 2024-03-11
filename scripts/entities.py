import pygame as pg

class Atom:
    def __init__(self, game, x, y, type):
        self.game = game
        self.x = x
        self.y = y
        self.type = type
        self.n_connections = self.game.n_connections[self.type]
        self.connections = [0,0,0,0] #up, down, left, right

    def check_move(self, molecule):
        space = self.game.level.matrix[self.y + (self.game.movement[0] + self.game.movement[1])][self.x + (self.game.movement[2] + self.game.movement[3])]
        if space == None:
            return True
        elif space in molecule:
            return True
        elif isinstance(space, Atom):
            if ((sum(self.connections) >= self.n_connections) and (space.check_move(molecule))):
                space.update()
                return True
        return False
        
    def move(self):
        new_x = self.x + (self.game.movement[2] + self.game.movement[3])
        new_y = self.y + (self.game.movement[0] + self.game.movement[1])
        self.x = new_x
        self.y = new_y
        
        
        for connection in self.connections:
            connection.update() 
        
    
    def update(self):
        self.move()

    def render(self, screen):
        screen.blit(self.game.assets[self.type], [self.x * 60 + 130, self.y * 60])
        screen.blit(self.game.assets[str(self.n_connections)], [self.x * 60 + 130, self.y * 60])
        
        
class Wall:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.type = "wall"
        
    def render(self, screen):
        screen.blit(self.game.assets['wall'], [self.x * 60 + 130, self.y * 60])        

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