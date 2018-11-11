from sys import argv
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


class Rectangle:
    height = 0
    wdith = 0
    x = 0
    y = 0

    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y


def main():
    with open('25PrecentFill.txt', 'r', encoding='utf-8') as input:
        fileContents = input.read().split('\n')
    height = fileContents[0].split(',')[0]
    width = fileContents[0].split(',')[1]
    # canvas = CustomCanvas(int(height), int(width))
    rectangleList = []
    for index in range(1, len(fileContents)):
        retangleSize = fileContents[index].split(',')
        rectangleList.append((retangleSize[0], retangleSize[1]))


main()
