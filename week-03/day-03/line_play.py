from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def draw_purple_line(x, range_start, range_end):
    line1 = canvas.create_line(x, range_start, range_end, x, fill="purple")

def draw_green_line(x):
    line2 = canvas.create_line(0, x, x, 300, fill="green")

for i in range(0, 300, 20):
    draw_purple_line(i, 0, 300)
    draw_green_line(i)

root.mainloop()
