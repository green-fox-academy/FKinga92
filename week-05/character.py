import random

class Character(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move_up(self):
        self.y -= 72
    
    def move_down(self):
        self.y += 72

    def move_left(self):
        self.x -= 72
    
    def move_right(self):
        self.x += 72
    
class Hero(Character):

    def __init__(self, x, y):
        d6 = random.randint(1, 6)
        super().__init__(x, y)
        self.image = "hero-down.gif"
        self.health_point = 20 + 3 * d6
        self.defend_point = 2 * d6
        self.strike_point = 5 + d6
