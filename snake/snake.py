from link_list import LinkedList


class Snake(LinkedList):
    def __init__(position: tuple[int, int]):
        super().__init__(data=position)

    def eatApple(self, apple: tuple[int, int]):
        self.append(apple)
    
    def move(self, move: tuple[int, int]):
        self.append(move)
        self.delete()