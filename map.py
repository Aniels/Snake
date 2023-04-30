from random import randrange


# a class make sure game role
class Map:

    def __init__(self, size) -> None:
        self.size = size
        self.apple:tuple
        self.new_apple()
        
    # design patten of factory method
    @classmethod
    def new_map(cls, size):
        return cls(size)

    def is_in_bounder(self, position) -> bool:
        if position[0] >= self.size or position[0] <= 0:
            return False
        elif position[1] >= self.size or position[1] <= 0:
            return False
        else:
            return True

    def is_not_body(self, position) -> bool:
        # tree.search(apple)
        pass

    def is_collision(cls) -> bool:
        if cls.is_in_bounder and cls.is_not_body:
            return True
        else:
            return False
    
    def new_apple(self) -> None:
        # generate a new apple position and return x, y position by tuple
        new_apple = randrange(0, self.size)
        self.apple = new_apple
    
    def ate_apple(self, apple) -> None:
        # tree.insert(apple)
        pass