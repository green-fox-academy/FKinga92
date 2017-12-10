# reproduce this: https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/recursion/drawing/graphic.png

from tkinter import *
import math

root = Tk()

SIZE = 900

canvas = Canvas(root, width=SIZE, height=SIZE)
canvas.pack()

hexa_side = SIZE // 3
height = int(2 * (math.sqrt(hexa_side ** 2 - (hexa_side / 2) ** 2)))
m = height // 2
x1 = 250
y1 = 100

def draw_hexa(x,y,size, m):
    canvas.create_polygon(x, y,
                          x + size, y,
                          x + 3/2 * size, y + m,
                          x + size, y + 2 * m,
                          x, y + 2 * m,
                          x - size / 2, y + m,
                          fill="white", width="1", outline="black")

def draw(offset_x, offset_y, size, m):
    if size < 25:
        return
    unit = size / 2
    unit_h = m / 2
    
    draw_hexa(x1 + offset_x, y1 + offset_y, unit, unit_h)
    draw_hexa(x1 + 3 * unit / 2 + offset_x, y1 + unit_h + offset_y, unit, unit_h)
    draw_hexa(x1 + offset_x, y1 + 2 * unit_h + offset_y, unit, unit_h)
    
    draw(offset_x,
         offset_y,
         unit, unit_h)
    draw(3 * unit / 2 + offset_x,
              unit_h + offset_y,
              unit, unit_h)
    draw(offset_x,
        2 * unit_h + offset_y,
        unit, unit_h)

draw_hexa(x1 , y1 , hexa_side, m)
draw(0, 0, hexa_side, m)
root.mainloop()