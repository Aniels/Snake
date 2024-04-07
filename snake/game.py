# handle general event for game
import sys
import pygame
from .interface import Interface


class Game:
    def __init__(self) -> None:
        # Initial the game property
        self.score = 0
        self.interface = Interface()

    @staticmethod
    def process_input():
        pass

    @staticmethod
    def modify_status():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):

        self.interface.show_score(self.score)
        # Update the display
        pygame.display.flip()

    # Main game loop
    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()
            self.clock.tick(10000)
    # Cap the frame rate

    def start(self):
        self.clock = pygame.time.Clock()  # Initialize the clock
        self.game_loop()  # Start the game loop