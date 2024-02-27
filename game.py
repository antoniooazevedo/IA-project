import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pygame Template")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player
player_x = 40
player_y = 40
block_size = 40

# Define level layout
level_layout = [
    (80, 80, 600, block_size),  # Top wall
    (80, 80, block_size, 400),   # Left wall
    (680, 80, block_size, 400),   # Right wall
    (80, 480, 640, block_size)    # Bottom wall
]

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= block_size
            elif event.key == pygame.K_RIGHT:
                player_x += block_size
            elif event.key == pygame.K_UP:
                player_y -= block_size
            elif event.key == pygame.K_DOWN:
                player_y += block_size
    # Draw
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, block_size, block_size))

    for wall in level_layout:
        pygame.draw.rect(screen, BLACK, wall)
    # Draw code here

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
