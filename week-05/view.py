import random
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
       self.monster_image = PhotoImage(file="skeleton.gif")
       self.boss_image = PhotoImage(file="boss.gif")
       self.hero = Hero(36, 36)
       self.map = Map(36, 36)
       self.map.fill_map()
       self.monster_tile = None
       self.monster = None
       self.monsters = []
       self.boss_tile = None
       self.boss = None
       self.movement_count = 0
    
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
    
    def draw_monsters(self):
        for monster in self.monsters:
            canvas.create_image(monster.x, monster.y, image=self.monster_image)
    
    def draw_boss(self):
        canvas.create_image(self.boss.x, self.boss.y, image=self.boss_image)
    
    #ezt majd át kell tenni game_logicba vagy characterbe(?)
    def create_monsters(self):
        for i in range(0, 3):
            monster_tile = self.map.get_random_floor()
            while not isinstance(monster_tile, Floor):
                monster_tile = self.map.get_random_floor()
            self.monster_tile = monster_tile
            self.monster = Monster(self.monster_tile.x, self.monster_tile.y)
            self.monsters.append(self.monster)

    def create_boss(self):
        boss_tile = self.map.get_random_floor()
        while not isinstance(boss_tile, Floor):
            boss_tile = self.map.get_random_floor()
        self.boss_tile = boss_tile
        self.boss = Monster(self.boss_tile.x, self.boss_tile.y)
    
    def move_monsters(self, movement_count):
        if movement_count % 2 == 0 and movement_count > 0:
            for monster in self.monsters:
                direction_chance = random.randint(1, 4)
                if direction_chance == 1 and monster.y > 36 and isinstance(self.map.get_tile_at_x_y(monster.x, monster.y - 72), Floor):
                    monster.move_up()
                elif direction_chance == 2 and monster.y < 684 and isinstance(self.map.get_tile_at_x_y(monster.x, monster.y + 72), Floor):
                    monster.move_down()
                elif direction_chance == 3 and monster.x > 36 and isinstance(self.map.get_tile_at_x_y(monster.x - 72, monster.y), Floor):
                    monster.move_left()
                elif direction_chance == 4 and monster.x < 684 and isinstance(self.map.get_tile_at_x_y(monster.x + 72, monster.y), Floor):
                    monster.move_right()
                    
    def move_boss(self, movement_count):
        if movement_count % 2 == 0 and movement_count > 0:
            direction_chance = random.randint(1, 4)
            if direction_chance == 1 and self.boss.y > 36 and isinstance(self.map.get_tile_at_x_y(self.boss.x, self.boss.y - 72), Floor):
                self.boss.move_up()
            elif direction_chance == 2 and self.boss.y < 684 and isinstance(self.map.get_tile_at_x_y(self.boss.x, self.boss.y + 72), Floor):
                self.boss.move_down()
            elif direction_chance == 3 and self.boss.x > 36 and isinstance(self.map.get_tile_at_x_y(self.boss.x - 72, self.boss.y), Floor):
                self.boss.move_left()
            elif direction_chance == 4 and self.boss.x < 684 and isinstance(self.map.get_tile_at_x_y(self.boss.x + 72, self.boss.y), Floor):
                self.boss.move_right()


    def on_key_press(self, e):
        self.draw_map(self.map)
        self.draw_monsters()
        self.draw_boss()
        if e.keycode == 38:
            if self.hero.y > 36 and isinstance(self.map.get_tile_at_x_y(self.hero.x, self.hero.y - 72), Floor):
                self.hero.move_up()
                self.movement_count += 1
            self.draw_hero_up(Hero(self.hero.x, self.hero.y))
        elif e.keycode == 40:
            if self.hero.y < 684 and isinstance(self.map.get_tile_at_x_y(self.hero.x, self.hero.y + 72), Floor):
                self.hero.move_down()
                self.movement_count += 1
            self.draw_hero_down(Hero(self.hero.x, self.hero.y))
        elif e.keycode == 37:
            if self.hero.x > 36 and isinstance(self.map.get_tile_at_x_y(self.hero.x - 72, self.hero.y), Floor):
                self.hero.move_left()
                self.movement_count += 1
            self.draw_hero_left(Hero(self.hero.x, self.hero.y))
        elif e.keycode == 39:
            if self.hero.x < 684 and isinstance(self.map.get_tile_at_x_y(self.hero.x + 72, self.hero.y), Floor):
                self.hero.move_right()
                self.movement_count += 1
            self.draw_hero_right(Hero(self.hero.x, self.hero.y))
        self.move_monsters(self.movement_count)
        self.move_boss(self.movement_count)
        
        

view = View()
canvas.bind("<KeyPress>", view.on_key_press)
canvas.pack()
canvas.focus_set()
view.draw_map(view.map)
view.draw_hero_down(view.hero)
view.create_monsters()
view.create_boss()
view.draw_monsters()
view.draw_boss()

root.mainloop()
