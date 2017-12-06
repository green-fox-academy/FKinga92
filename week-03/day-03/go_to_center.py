from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def draw_line(x, y):
    your_line = canvas.create_line(x, y, 150, 150)

draw_line(15, 15)
draw_line(50, 75)
draw_line(0, 150)
root.mainloop()
