from tkinter import *


class CustomCanvas:
    height = 0
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width
        root = Tk()
        root.geometry(str(height) + 'x' + str(width))
        canvas = Canvas(root, height=height, width=width, bg='white')
        canvas.pack()
        root.mainloop()
canvas = CustomCanvas(200, 200)
