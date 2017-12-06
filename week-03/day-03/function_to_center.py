from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bd='0')
canvas.pack()

#  create a line drawing function that takes 2 parameters:
#  the x and y coordinates of the line's starting point
#  and draws a line from that point to the center of the canvas.
#  fill the canvas with lines from the edges, every 20 px, to the center.

def draw_line(x, y):
    canvas.create_line(x, y, 150, 150)

x_list = [0, 300]
y_list = [0, 300]
for i in y_list:
    y = i
    x = 0
    for j in range(15):
        draw_line(x, y)
        x += 20
for i in x_list:
    x = i
    y = 0
    for j in range(15):
        draw_line(x, y)
        y += 20
draw_line(300, 300)
root.mainloop()
