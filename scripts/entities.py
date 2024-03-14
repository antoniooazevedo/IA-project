import pygame as pg

class Atom:
    def __init__(self, game, x, y, type):
        self.game = game
        self.x = x
        self.y = y
        self.type = type
        self.n_connections = self.game.n_connections[self.type]
        self.connections = []

    def check_move(self, molecule):
        space = self.game.level.matrix[self.y + (self.game.movement[0] + self.game.movement[1])][self.x + (self.game.movement[2] + self.game.movement[3])]
        if space == None:
            return (True, [])
        elif space in molecule:
            return (True, [])
        elif isinstance(space, Atom):
            if (len(self.connections) >= self.n_connections):
                (can_move, atoms) = space.check_move(molecule)
                return (can_move, [space] + atoms)
        return (False, [])
        
    #def check_move_outside_molecule(self, atom)    
    
    def move(self):
        new_x = self.x + (self.game.movement[2] + self.game.movement[3])
        new_y = self.y + (self.game.movement[0] + self.game.movement[1])
        self.game.level.matrix[self.y][self.x] = None
        self.game.level.matrix[new_y][new_x] = self
        self.x = new_x
        self.y = new_y
        
        for connection in self.connections:
            connection.update() 
    
    def update(self):
        self.move()

    def render(self, screen):
        screen.blit(self.game.assets[self.type], [self.x * 60 + 130, self.y * 60])
        if (self.n_connections - len(self.connections) > 0):
            screen.blit(self.game.assets[str(self.n_connections - len(self.connections))], [self.x * 60 + 130, self.y * 60])
        for connection in self.connections:
            connection.render(screen)
            
    def get_connection(self, connection):
        if connection.direction == "up":
            return self.game.level.matrix[self.y - 1][self.x]
        elif connection.direction == "down":
            return self.game.level.matrix[self.y + 1][self.x]
        elif connection.direction == "left":
            return self.game.level.matrix[self.y][self.x - 1]
        elif connection.direction == "right":
            return self.game.level.matrix[self.y][self.x + 1]
        
        
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
        screen.blit(self.game.assets[self.direction], [self.x * 60 + 130, self.y * 60])
        
    def update(self):
        
        new_x = self.x + (self.game.movement[2] + self.game.movement[3])
        new_y = self.y + (self.game.movement[0] + self.game.movement[1])
        self.y = new_y
        self.x = new_x  