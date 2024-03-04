import pygame

class Atom:
    def __init__(self, game, x, y, type, connections=1):
        self.game = game
        self.x = x
        self.y = y
        self.type = type
        self.n_connections = connections
        self.n_connections = [0,0,0,0] #up, down, left, right
    
    def update(self, movement=[0, 0, 0, 0]):

        new_x = self.x + (movement[1] + movement[0])
        new_y = self.y + (movement[3] + movement[2])

        self.movement = [0, 0, 0, 0]

        player_rect = pygame.Rect(new_x, new_y, self.game.block_size, self.game.block_size)
        for wall in self.game.level_layout:
            wall_rect = pygame.Rect(*wall)
            print(player_rect.colliderect(wall_rect))
            if (player_rect.colliderect(wall_rect)):
                return    
        self.y = new_x
        self.x = new_y  
        

    def render(self, screen):
        screen.blit(self.game.assets['player'], [self.x, self.y])
        
