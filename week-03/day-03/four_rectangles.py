from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
canvas.create_rectangle(3, 3, 21, 26, fill="red")
canvas.create_rectangle(35, 35, 85, 75, fill="green")
canvas.create_rectangle(50, 85, 150, 130, fill="blue")
canvas.create_rectangle(150, 140, 300, 300, fill="yellow")

root.mainloop()
