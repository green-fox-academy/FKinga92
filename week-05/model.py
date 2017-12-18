class Tile(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Floor(Tile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.can_be_occupied = True

class Wall(Tile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.can_be_occupied = False

class Map(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.map = [
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]
    
