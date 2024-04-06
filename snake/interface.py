import pygame

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Snake and food properties
block_size = 20
snake_speed = 10

# Fonts
font = pygame.font.SysFont(None, 30)

# Function to display message on screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width / 6, screen_height / 3])


# Function to display score
def show_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [0, 0])

# Function to display game over message
def game_over():
    message_to_screen("Game Over! Press C to play again or Q to quit", red)