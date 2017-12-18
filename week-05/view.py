from tkinter import *
from map import *
from character import *

root = Tk()
canvas = Canvas(root, width=720, height=720)

class View(object):

    def __init__(self):
       self.floor = PhotoImage(file="floor.gif")
       self.wall = PhotoImage(file="wall.gif")
       self.hero = PhotoImage(file="hero-down.gif")

    # def draw_tile(self, tile):
    #     if not isinstance(tile, Tile):
    #         return
    #     self.img = PhotoImage(file=tile.image)
    #     canvas.create_image(tile.x, tile.y, image=self.img)
    
    def draw_map(self, map):
        if not isinstance(map, Map):
            return
        for i in range(len(map.map)):
            for j in range(len(map.map[i])):
                x = map.x + j * 72
                y = map.y + i * 72
                if map.map[i][j] == 0:
                    canvas.create_image(x, y, image=self.floor)
                else:
                    canvas.create_image(x, y, image=self.wall)
    
    def draw_hero(self, hero):
        canvas.create_image(hero.x, hero.y, image=self.hero)


view = View()
map = Map(36, 36)
the_hero = Hero(36, 36)
canvas.pack()
view.draw_map(map)
view.draw_hero(the_hero)

root.mainloop()