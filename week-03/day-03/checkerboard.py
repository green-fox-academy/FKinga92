from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def draw_rectangle(x, y, colour1):
    canvas.create_rectangle(x, y, x + 37, y + 37, fill=colour1)

x = 3
y = 3
colour_bool = True

for row in range(8):
    for col in range(8):
        if colour_bool:
            colour1 = "white"
        else:
            colour1 = "black"
        if col < 7:
            draw_rectangle(x, y, colour1)
            x += 37
        else:
            draw_rectangle(x, y, colour1)
            x = 3
        colour_bool = not colour_bool 
    y += 37
    colour_bool = not colour_bool

root.mainloop()
