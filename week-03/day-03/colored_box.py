from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
red_line = canvas.create_line(15, 15, 150, 15, fill='red')
blue_line = canvas.create_line(15, 15, 15, 200, fill='blue')
teal_line = canvas.create_line(15, 200, 150, 200, fill='light sea green')
yellow_line = canvas.create_line(150, 200, 150, 15, fill='yellow')

root.mainloop()
