from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def draw_center_box(x):
    your_box = canvas.create_rectangle((150 - x/2), (150 - x/2), (150 + x/2), (150 + x/2))

draw_center_box(25)
draw_center_box(50)
draw_center_box(200)

root.mainloop()
