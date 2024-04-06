from random import randrange


# a class make sure game role
class Map:

    def __init__(self, size: tuple[int, int]):
        self.size = size
        self.apple: tuple
        
    # design patten of factory method
    @classmethod
    def new_map(cls, size):
        return cls(size)

    def is_in_bounder(self, position) -> bool:
        if position[0] >= self.size or position[0] <= 0:
            return False
        return not (position[1] >= self.size or position[1] <= 0)

    @staticmethod
    def is_not_body(position) -> bool:
        pass

    def is_collision(cls) -> bool:
        return cls.is_in_bounder and cls.is_not_body
    
    def new_apple(self) -> None:
        # generate a new apple position and return x, y position by tuple
        new_apple = randrange(0, self.size)
        self.apple = new_apple
    
    @staticmethod
    def ate_apple(apple) -> None:
        pass