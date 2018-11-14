from sys import argv
from tkinter import *

from rectpack import newPacker

import rpack


class Rectangle:
    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def setOrigin(self, x, y):
        self.x = x
        self.y = y


class CustomCanvas:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.geometry(str(height) + 'x' + str(width))
        self.canvas = Canvas(self.root, height=height, width=width, bg='white')

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
    for rect in allRect:
        rectangleList.append((rect.height, rect.width))

    positions = rpack.pack(rectangleList)
    for index in range(0, len(allRect)):
        rect = allRect[index]
        pos = positions[index]
        rect.x = pos[0]
        rect.y = pos[1]

    # packer = newPacker()

    # # Add the rectangles to packing queue
    # for r in rectangleList:
    #     packer.add_rect(r)

    # # Add the bins where the rectangles will be placed

    # packer.add_bin(canvasSize)

    # # Start packing
    # packer.pack()
    # print(nrect=len(packer[0]))
    return allRect


def main():
    with open(argv[1], 'r', encoding='utf-8') as input:
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
    # canvas.addRectangle(placedRectangleList[3])

    canvas.displayCanvas()


if __name__ == '__main__':
    main()
