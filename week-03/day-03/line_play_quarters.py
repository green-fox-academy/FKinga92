from tkinter import *

root = Tk()

size = 300
s2 = size // 2
canvas = Canvas(root, width=size, height=size)
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def quarter(x1, y1, x2, y2):
    for i in range(0, s2, 10):
        purple_line = canvas.create_line(x1 + i, y1, x2, y1 + i, fill="purple")
        green_line = canvas.create_line(x1, y1 + i, x1 + i, y2, fill="green")

quarter(0, 0, s2, s2)
quarter(0, s2, s2, size)
quarter(s2, 0, size, s2)
quarter(s2, s2, size, size)

root.mainloop()

