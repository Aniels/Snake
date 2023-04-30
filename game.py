# handle general event for game

from map import Map as map

class game:
    def __init__(cls, size) -> None:
        cls.map = map.new_map(size=size)
        cls.count = 0

    def move():
        pass

    def ate_apple(cls):
        cls.count += 1
        cls.map.new_apple


