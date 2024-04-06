# handle general event for game
import sys
import map
import pygame 


# Set up the display
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# set up the snake
SNAKE_INIT_LOCATION = [(5, 5)]

class Game:
    def __init__(self, size) -> None:

        # Initial the game property
        pygame.init()  # Initialize Pygame
        self.score = 0
       
        # Set up the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.snake = SNAKE_INIT_LOCATION

    def processInput(self):
        pass

    def modifyStatus(self):
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        # Clear the screen
        self.screen.fill(BACKGROUND_COLOR)

        # Draw the snake
        self.drawSnake(self.snake)

        # Update the display
        pygame.display.flip()

    # Main game loop
    def gameLoop(self):
        while pygame.QUIT:
            self.processInput
            self.modifyStatus
            self.draw
            self.clock.tick(10)  # Cap the frame rate

    def start(self):
       self.clock = pygame.time.Clock()  # Initialize the clock
       self.game_loop()  # Start the game loop
    
    # Function to draw the snake
    def drawSnake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, SNAKE_COLOR, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
