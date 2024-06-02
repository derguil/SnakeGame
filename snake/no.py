import pygame
import sys
import time
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

snake_width = 20
snake_height = 20
snake_x = screen_width // 2
snake_y = screen_height // 2
to_X = 0
to_Y = 0
snake_length = 1

snake_x_size = [snake_x]
snake_y_size = [snake_y]

apple_width = 20
apple_height = 20
apple_x = screen_width // 2
apple_y = screen_height // 2

apple_x,apple_y = (random.randint(0,39)*20, random.randint(0,29)*20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_X = -snake_width
                to_Y = 0
            if event.key == pygame.K_RIGHT:
                to_X = snake_width
                to_Y = 0
            if event.key == pygame.K_UP:
                to_X = 0
                to_Y = -snake_width
            if event.key == pygame.K_DOWN:
                to_X = 0
                to_Y = snake_width

    snake_x += to_X
    snake_y += to_Y
    
    snake_x_size.append(snake_x)
    snake_y_size.append(snake_y)

    if snake_x < 0 or snake_x >= 800 or snake_y < 0 or snake_y >= 600:
        running = False

    if apple_x == snake_x and apple_y == snake_y:
        snake_length += 1
        apple_x,apple_y = (random.randint(0,39)*20, random.randint(0,29)*20)
    else:
        snake_x_size.pop(0)
        snake_y_size.pop(0)
        
    screen.fill(BLACK)
    for i in range(snake_length):
        pygame.draw.rect(screen, WHITE, [snake_x_size[i], snake_y_size[i], snake_width, snake_height])
    pygame.draw.rect(screen, RED, [apple_x, apple_y, apple_width, apple_height])
    pygame.display.flip()
    
    time.sleep(0.2)
pygame.quit()
sys.exit()
