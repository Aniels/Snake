import pygame


# Set up the display
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake and food properties
block_size = 20
snake_speed = 10

class Interface:
    def __init__(self) -> None:
        pygame.init()
        # Set up the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.screen.fill(WHITE)
        # Fonts
        self.font = pygame.font.SysFont("Board", 30)

    # Function to display message on screen
    def message_to_screen(self, msg, color):
        screen_text = self.font.render(msg, True, color)
        self.screen.blit(screen_text, [WIDTH / 6, HEIGHT / 3])

    # Function to display score
    def show_score(self, score):
        self.screen.fill(BACKGROUND_COLOR)  # Clear the screen
        score_text = self.font.render("Score: " + str(score), True, BLACK)
        self.screen.blit(score_text, [0, 0])

    # Function to display game over message
    def game_over(self):
        self.message_to_screen("Game Over! Press C to play again or Q to quit", RED)

    # Function to draw the snake

    def draw_snake(self, snake):
        for segment in snake:
            pygame.draw.rect(
                self.screen,
                SNAKE_COLOR,
                (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
            )