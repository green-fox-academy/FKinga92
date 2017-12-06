from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300',  bd=0)
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

def connect_the_dots(alist):
    for i in range(len(alist)):
        if i < (len(alist) -1):
            x, y = alist[i][0], alist[i][1]
            x2, y2 = alist[i+1][0], alist[i+1][1]
            line1 = canvas.create_line(x, y, x2, y2)
        else:
            x, y = alist[i][0], alist[i][1]
            x2, y2 = alist[0][0], alist[0][1]
            line1 = canvas.create_line(x, y, x2, y2)


connect_the_dots([[10, 10], [290,  10], [290, 290], [10, 290]])
connect_the_dots([[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]])



root.mainloop()
