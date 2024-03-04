import pygame
import sys
import scripts.entities as Atom
import scripts.utils as utils

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
    
        pygame.display.set_caption("Sokobond")

        self.clock = pygame.time.Clock()

        self.movement = [0, 0, 0, 0]

        self.assets = {
            "player": utils.load_image("base_sprite.png")
        }

        self.player = Atom(self, self.player_x, self.player_y, "player", 1)

        #self.screen = pygame.display.set_mode(WINDOW_SIZE)
        #self.player_x, self.player_y = 120, 120


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

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.movement[0] = -32
            elif event.key == pygame.K_DOWN:
                self.movement[1] = 32
            elif event.key == pygame.K_LEFT:
                self.movement[2] = -32
            elif event.key == pygame.K_RIGHT:
                self.movement[3] = 32

    def draw(self):
        self.screen.fill(WHITE)

        self.player.update(self.movement)
        self.player.render(self.screen)

        for wall in level_layout:
            pygame.draw.rect(self.screen, BLACK, wall)

        pygame.display.flip()

Game().run();