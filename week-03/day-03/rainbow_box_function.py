from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def draw_square(x, colour1):
    your_square = canvas.create_rectangle((150 - int(x)/2), (150 - int(x)/2),
                                          (150 + int(x)/2), (150 + int(x)/2), fill=str(colour1))


rainbow_list = {"120":"red", "80":"yellow", "50":"pink", "40":"green", "30":"purple", "20":"orange", "10":"blue"}

for size, colour in rainbow_list.items():
        draw_square(size, colour)

root.mainloop()
