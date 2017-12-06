from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def draw_square(x, y):
    your_square = canvas.create_rectangle(x, y, x+50, y+50)


draw_square(5, 5)
draw_square(60, 60)
draw_square(150, 150)

root.mainloop()
