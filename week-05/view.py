from tkinter import *
from area import *
from character import *

root = Tk()
canvas = Canvas(root, width=720, height=720)

class View(object):

    def __init__(self):
       self.floor = PhotoImage(file="floor.gif")
       self.wall = PhotoImage(file="wall.gif")
       self.hero_image = PhotoImage(file="hero-down.gif")
       self.hero = Hero(36, 36)
       self.map = Map(36, 36)
    
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
        canvas.create_image(hero.x, hero.y, image=self.hero_image)
    
    def on_key_press(self, e):
        if e.keycode == 38:
            self.hero.move_up()
        elif e.keycode == 40:
            self.hero.move_down()
        elif e.keycode == 37:
            self.hero.move_left()
        elif e.keycode == 39:
            self.hero.move_right()
        self.draw_map(self.map)
        self.draw_hero(Hero(self.hero.x, self.hero.y))


view = View()
canvas.bind("<KeyPress>", view.on_key_press)
canvas.pack()
canvas.focus_set()
view.draw_map(view.map)
view.draw_hero(view.hero)

root.mainloop()