import pygame
from link_list import LinkedList

# set up the snake
SNAKE_INIT_LOCATION = (5, 5)

class Snake(LinkedList, pygame.sprite.Sprite):
    def __init__():
        super().__init__()

    @staticmethod
    def get():
        return Snake().append(data=SNAKE_INIT_LOCATION)

    def eatApple(self, apple: tuple[int, int]):
        self.append(apple)
    
    def move(self, next: tuple[int, int]):
        self.append(next)
        self.delete()