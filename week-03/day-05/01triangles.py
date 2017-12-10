from tkinter import *
import math
import random

root = Tk()

SIZE = 600

canvas = Canvas(root, width=SIZE, height=SIZE, bg="white")
canvas.pack()

def draw_triangle(x, y, size):
    height = math.sqrt(size ** 2 - (size / 2) ** 2)
    canvas.create_polygon(
        x, y,
        x + size, y,
        x + size / 2, y + height,
        outline='black', fill="#%06x" % random.randint(0, 0xFFFFFF), width="1"
    )

def draw(x, y, size):
    if size < 15:
        return
    unit = size / 2
    height = math.sqrt(unit ** 2 - (unit / 2) ** 2)
    draw_triangle(x, y, unit)
    draw_triangle(x + unit, y, unit)
    draw_triangle(x + unit / 2, y + height, unit)

    draw(x, y, unit)
    draw(x + unit, y, unit)
    draw(x + unit / 2, y + height, unit)

draw(0, 0, SIZE)

root.mainloop()