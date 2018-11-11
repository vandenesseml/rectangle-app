from sys import argv
from tkinter import *


class Rectangle:
    height = 0
    width = 0
    x = 0
    y = 0

    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y


class CustomCanvas:
    height = 0
    width = 0
    canvas = None
    root = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.geometry(str(height) + 'x' + str(width))
        self.canvas = Canvas(self.root, height=height, width=width, bg='white')
        self.canvas.create_rectangle(25, 25, 50, 50)

    def addRectangle(self, rectangle):
        x1 = rectangle.x
        y1 = rectangle.y
        x2 = x1 + rectangle.width
        y2 = y1 + rectangle.height
        self.canvas.create_rectangle(x1, y1, x2, y2)

    def displayCanvas(self):
        self.canvas.pack()
        self.root.mainloop()


def pack(allRect, canvasSize):
    rectangleList = []

    return allRect


def main():
    with open('25PrecentFill.txt', 'r', encoding='utf-8') as input:
        fileContents = input.read().split('\n')
    height = int(fileContents[0].split(',')[0])
    width = int(fileContents[0].split(',')[1])
    canvasSize = (height, width)
    canvas = CustomCanvas(height, width)
    rectangleList = []
    for index in range(1, len(fileContents)):
        rectangleSize = fileContents[index].split(',')
        rectangle = Rectangle(
            int(rectangleSize[0]), int(rectangleSize[1]), 0, 0)
        rectangleList.append(rectangle)
    placedRectangleList = pack(rectangleList, canvasSize)

    for rectangle in placedRectangleList:
        canvas.addRectangle(rectangle)

    canvas.displayCanvas()


main()
