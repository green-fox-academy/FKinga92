from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def draw_rectangle(x, y, s):
    canvas.create_rectangle(x, y, x + int(s), y+ int(s), fill="medium orchid")

x = 11
y = 11
s = 11
for i in range(6):
    draw_rectangle(x, y, s)
    x += s
    y += s
    s += 10
    

root.mainloop()
