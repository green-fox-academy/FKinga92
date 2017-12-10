from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bd=0)
canvas.pack()
canvas_size = 300
triangle_size = int(canvas_size / 21)
# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]

def draw_triangle(x, y, size):
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, fill="white", width="1", outline="black")


for row in range(21):
    for i in range(3 + (row * 7), canvas_size - 3 - (row * 7), triangle_size):
        draw_triangle(i, 300 - (row * 14), triangle_size)


root.mainloop()
