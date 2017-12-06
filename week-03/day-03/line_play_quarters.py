from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def draw_purple_line1(x, range_start, range_end):
    line1 = canvas.create_line(x, range_start, range_end, x, fill="purple")

def draw_green_line1(x, range_start, range_end):
    line2 = canvas.create_line(range_start, x, x, range_end, fill="green")

def draw_purple_line2(x, range_start, range_end):
    line1 = canvas.create_line(x, 0, range_end, x-range_start, fill="purple")

def draw_green_line2(x, range_end):
    line2 = canvas.create_line(range_end, x, range_end+x, range_end, fill="green")

def draw_purple_line3(x, range_end):
    line1 = canvas.create_line(x, range_end, range_end, range_end+x, fill="purple")

def draw_green_line3(x, range_start, range_end):
    line2 = canvas.create_line(0, x, x-range_start, range_end, fill="green")

for i in range(0, 150, 20):
    draw_purple_line1(i, 0, 150)
    draw_green_line1(i, 0, 150)
    draw_green_line2(i, 150)
    draw_purple_line3(i, 150)
    
for i in range(150, 300, 20):
    draw_purple_line1(i, 150, 300)
    draw_green_line1(i, 150, 300)
    draw_purple_line2(i, 150, 300)
    draw_green_line3(i, 150, 300)

# hétvégén átalakítom :)
   




root.mainloop()
