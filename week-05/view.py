from tkinter import *
from area import *
from character import *

root = Tk()
canvas = Canvas(root, width=720, height=720)

class View(object):

    def __init__(self):
       self.floor = PhotoImage(file="floor.gif")
       self.wall = PhotoImage(file="wall.gif")
       self.hero_image_down = PhotoImage(file="hero-down.gif")
       self.hero_image_up = PhotoImage(file="hero-up.gif")
       self.hero_image_left = PhotoImage(file="hero-left.gif")
       self.hero_image_right = PhotoImage(file="hero-right.gif")
       self.hero = Hero(36, 36)
       self.map = Map(36, 36)
       self.map.fill_map()
    
    # def draw_map(self, map):
    #     if not isinstance(map, Map):
    #         return
    #     for i in range(len(map.map)):
    #         for j in range(len(map.map[i])):
    #             x = map.x + j * 72
    #             y = map.y + i * 72
    #             if map.map[i][j] == 0:
    #                 canvas.create_image(x, y, image=self.floor)
    #             else:
    #                 canvas.create_image(x, y, image=self.wall)
    def draw_map(self, map):
        if not isinstance(map, Map):
            return
        for tile in map.map_of_tiles:
            if isinstance(tile, Floor):
                canvas.create_image(tile.x, tile.y, image=self.floor)
            else:
                canvas.create_image(tile.x, tile.y, image=self.wall)

    def draw_hero_down(self, hero):
        canvas.create_image(hero.x, hero.y, image=self.hero_image_down)

    def draw_hero_up(self, hero):
        canvas.create_image(hero.x, hero.y, image=self.hero_image_up)

    def draw_hero_left(self, hero):
        canvas.create_image(hero.x, hero.y, image=self.hero_image_left)

    def draw_hero_right(self, hero):
        canvas.create_image(hero.x, hero.y, image=self.hero_image_right)
    
    def on_key_press(self, e):
        self.draw_map(self.map)
        if e.keycode == 38:
            if self.hero.y > 36 and isinstance(self.map.get_tile_at_x_y(self.hero.x, self.hero.y - 72), Floor):
                self.hero.move_up()
            self.draw_hero_up(Hero(self.hero.x, self.hero.y))
        elif e.keycode == 40:
            if self.hero.y < 684 and isinstance(self.map.get_tile_at_x_y(self.hero.x, self.hero.y + 72), Floor):
                self.hero.move_down()
            self.draw_hero_down(Hero(self.hero.x, self.hero.y))
        elif e.keycode == 37:
            if self.hero.x > 36 and isinstance(self.map.get_tile_at_x_y(self.hero.x - 72, self.hero.y), Floor):
                self.hero.move_left()
            self.draw_hero_left(Hero(self.hero.x, self.hero.y))
        elif e.keycode == 39:
            if self.hero.x < 684 and isinstance(self.map.get_tile_at_x_y(self.hero.x + 72, self.hero.y), Floor):
                self.hero.move_right()
            self.draw_hero_right(Hero(self.hero.x, self.hero.y))
        

view = View()
canvas.bind("<KeyPress>", view.on_key_press)
canvas.pack()
canvas.focus_set()
view.draw_map(view.map)
view.draw_hero_down(view.hero)

root.mainloop()