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

def check_move(px, py, mv):
    new_px, new_py = px, py
    match mv: 
        case "R":
            new_px += block_size
        case "L":
            new_px -= block_size
        case "U":
            new_py -= block_size
        case "D":
            new_py += block_size
        case _:
            return (px, py)

    player_rect = pygame.Rect(new_px, new_py, block_size, block_size)
    for wall in level_layout:
        wall_rect = pygame.Rect(*wall)
        if player_rect.colliderect(wall_rect):
            return (px, py)  # Return old position if would collide with a wall

    return (new_px, new_py)  # Return new position if no collision

def handle_events():
    global player_x, player_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                (player_x, player_y) = check_move(player_x, player_y, "L")
            elif event.key == pygame.K_RIGHT:
                (player_x, player_y) = check_move(player_x, player_y, "R")
            elif event.key == pygame.K_UP:
                (player_x, player_y) = check_move(player_x, player_y, "U")
            elif event.key == pygame.K_DOWN:
                (player_x, player_y) = check_move(player_x, player_y, "D")
    return True

def draw(screen):
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, block_size, block_size))

    for wall in level_layout:
        pygame.draw.rect(screen, BLACK, wall)

    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Sokobond")
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events()
        draw(screen)
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()