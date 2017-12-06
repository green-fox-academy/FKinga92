from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black', bd=0)
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

def draw_stars(x, y, size, color1):
    canvas.create_rectangle(x, y, x+size, y+size, fill=color1)

for i in range(500):
    x = random.randrange(300)
    y = random.randrange(300)
    size = random.randrange(10)
    color1 = "grey" + str(random.randrange(99))
    draw_stars(x, y, size, color1)

root.mainloop()
