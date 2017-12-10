from tkinter import *
import math
import random

root = Tk()

canvas_size = 600
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

hexa_side = 280


def draw_hexa(x,y,size):
    height = int(2 * (math.sqrt(size ** 2 - (size / 2) ** 2)))
    m = height // 2
    canvas.create_polygon(x, y,
                          x + size, y,
                          x + 3/2 * size, y + m,
                          x + size, y + 2 * m,
                          x, y + 2 * m,
                          x - size / 2, y + m,
                          fill="#%03x" % random.randint(0, 0xFFF), width="1", outline="black")

def draw(x, y, size):
    if size < 5:
        return
    unit = size / 3
    height = 2 * (math.sqrt(unit ** 2 - (unit / 2) ** 2))

    draw_hexa(x, y, unit)
    draw_hexa(x + 2 * unit, y, unit)
    draw_hexa(x + 3 * unit, y + height, unit)
    draw_hexa(x + 2 * unit, y + 2 * height, unit)
    draw_hexa(x, y + 2 * height, unit)
    draw_hexa(x - unit, y + height, unit)

    draw(x, y, unit)
    draw(x + 2 * unit, y, unit)
    draw(x + 3 * unit, y + height, unit)
    draw(x + 2 * unit, y + 2 * height, unit)
    draw(x, y + 2 * height, unit)
    draw(x - unit, y + height, unit)


draw_hexa(150, 3, hexa_side)
draw(150, 3, hexa_side)

root.mainloop()