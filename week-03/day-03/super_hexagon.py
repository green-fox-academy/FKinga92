from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/super-hexagon/r6.gif]

canvas_size = 300
hexa_side = 20
height = int(2 * (math.sqrt(hexa_side ** 2 - (hexa_side / 2) ** 2)))
m = height // 2

def draw_hexa(x,y,size):
    canvas.create_polygon(x, y,
                          x + size, y,
                          x + 3/2 * size, y + m,
                          x + size, y + height,
                          x, y + height,
                          x - size / 2, y + m,
                          fill="white", width="1", outline="black")

for col in range(4):
    for i in range(7 - col):
        draw_hexa(130 - (col * 1.5 * hexa_side), 10 + (i * height) + (col * m), hexa_side)
    for i in range(7 - col):
        draw_hexa(130 + (col * 1.5 * hexa_side), 10 + (i * height) + (col * m), hexa_side)

root.mainloop()
