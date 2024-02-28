import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
block_size = 40

# Global variables
player_x = 120
player_y = 120
level_layout = [
    (80, 80, 600, block_size),  # Top wall
    (80, 80, block_size, 400),   # Left wall
    (680, 80, block_size, 400),   # Right wall
    (80, 480, 640, block_size)    # Bottom wall
]

class Game: 
    
    def __init__(self):
        pygame.init()
    
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Sokobond")
        self.clock = pygame.time.Clock()

        self.movement = [0, 0, 0, 0]
        self.player_x, self.player_y = 120, 120

    def run(self):
        while True:

            self.move()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pg.quit()
                    sys.exit()
                else:
                    self.event_handler(event)
                    
            self.clock.tick(FPS)
    
    def move(self):
        
        new_px = self.player_x + (self.movement[1] + self.movement[0]) * 4
        new_py = self.player_y + (self.movement[3] + self.movement[2]) * 4

        player_rect = pygame.Rect(new_px, new_py, block_size, block_size)
        for wall in level_layout:
            wall_rect = pygame.Rect(*wall)
            print(player_rect.colliderect(wall_rect))
            if (player_rect.colliderect(wall_rect)):
                return    
        self.player_x = new_px
        self.player_y = new_py
                
        

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.movement[0] = -1
            elif event.key == pygame.K_RIGHT:
                self.movement[1] = 1
            elif event.key == pygame.K_UP:
                self.movement[2] = -1
            elif event.key == pygame.K_DOWN:
                self.movement[3] = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.movement[0] = 0
            elif event.key == pygame.K_RIGHT:
                self.movement[1] = 0
            elif event.key == pygame.K_UP:
                self.movement[2] = 0
            elif event.key == pygame.K_DOWN:
                self.movement[3] = 0

    def draw(self):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, RED, (self.player_x, self.player_y, block_size, block_size))

        for wall in level_layout:
            pygame.draw.rect(self.screen, BLACK, wall)

        pygame.display.flip()

Game().run();