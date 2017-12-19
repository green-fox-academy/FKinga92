class Tile(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(type(self)) + str(self.x) + " " + str(self.y)

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
        self.map_of_tiles = []
    
    def fill_map(self):
         for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                x = self.x + j * 72
                y = self.y + i * 72
                if self.map[i][j] == 0:
                    self.map_of_tiles.append(Floor(x,y))
                else:
                    self.map_of_tiles.append(Wall(x,y))
