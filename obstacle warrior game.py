import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Obstacle Warrior Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    screen.fill(white)

    pygame.draw.rect(screen, red, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    pygame.draw.rect(screen, black, (player_x, player_y, player_width, player_height))

    obstacle_y += obstacle_speed

    if obstacle_y > screen_height:
        obstacle_y = 0
        obstacle_x = random.randint(0, screen_width - obstacle_width)

    if player_y < obstacle_y + obstacle_height:
        if player_x < obstacle_x < player_x + player_width or player_x < obstacle_x + obstacle_width < player_x + player_width:
            game_over = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
