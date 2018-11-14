from sys import argv
from tkinter import Canvas, Tk

from rectpack import newPacker


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
        self.canvas.create_rectangle(x1, y1, x2, y2, fill='yellow')

    def displayCanvas(self):
        self.canvas.pack()
        self.root.mainloop()


def pack(allRect, canvasSize):
    rectangleList = []
    for rect in allRect:
        rectangleList.append((rect.height, rect.width))
    packer = newPacker()

    for rectangle in rectangleList:
        packer.add_rect(*rectangle)

    packer.add_bin(*canvasSize)

    packer.pack()

    rectangleList = []
    for rectangle in packer.rect_list():
        rect = Rectangle(rectangle[4], rectangle[3], rectangle[1],
                         rectangle[2])
        rectangleList.append(rect)
    return rectangleList


def main():
    with open(argv[1], 'r', encoding='utf-8') as input:
        fileContents = input.read().split('\n')
    height = int(fileContents[0].split(',')[0])
    width = int(fileContents[0].split(',')[1])
    canvasSize = (height, width)
    canvas = CustomCanvas((height + 3), (width + 3))
    allRect = []
    for index in range(1, len(fileContents)):
        rectangleSize = fileContents[index].split(',')
        rectangle = Rectangle(int(rectangleSize[0]), int(rectangleSize[1]))
        allRect.append(rectangle)
    packedRectangles = pack(allRect, canvasSize)

    for rectangle in packedRectangles:
        canvas.addRectangle(rectangle)

    canvas.displayCanvas()


if __name__ == '__main__':
    main()
