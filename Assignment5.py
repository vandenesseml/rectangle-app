from sys import argv
from tkinter import Canvas, Tk

from rectpack import newPacker


# Rectangle class. Defines a rectangle object
class Rectangle:
    # Constructor creates rectangle object. Input = height, width, x and y.
    # width defines the width of the rectangle. Height defines the height
    # of the rectangle. X defines the horizontal origin with respect to the
    # top left corner. Y defines the vewrtical orgin with respect to the top
    # corner
    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    # setOrigin modifies the origin of a rectangle object. Input = x and y.
    # X defines the horizontal origin with respect to the top left corner. Y
    # defines the vewrtical orgin with respect to the top corner
    def setOrigin(self, x, y):
        self.x = x
        self.y = y


# CustomCanvas class. Defines a canvas object
class CustomCanvas:
    # Constructor creates canvas of specified hieght and width. Input = height
    # and width of type int. Background of canvas is set to white to
    # differentiate from the root
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.geometry(str(height) + 'x' + str(width))
        self.canvas = Canvas(self.root, height=height, width=width, bg='white')

    # Adds rectangle to canvas. Input = rectangle type Rectangle. Rectangles
    # will be drawn in yellow to help distinguish placement
    def addRectangle(self, rectangle):
        x1 = rectangle.x
        y1 = rectangle.y
        x2 = x1 + rectangle.width
        y2 = y1 + rectangle.height
        self.canvas.create_rectangle(x1, y1, x2, y2, fill='yellow')

    # Displays the canvas. Canvas is packed and then displayed
    def displayCanvas(self):
        self.canvas.pack()
        self.root.mainloop()


# pack function arranges rectangles within the canvas. Input = allRect and
# canvasSize. allRect defines a list of rectangles. canvasSize defines the
# specified canvas size the rectangles must be arranged in
def pack(allRect, canvasSize):
    rectangles = []
    # Create a list of tuples containing the height and width of the rectangles
    # received at input
    for rect in allRect:
        rectangles.append((rect.height, rect.width))
    packer = newPacker()
    # Add rectangles to rectangle packer import
    for rectangle in rectangles:
        packer.add_rect(*rectangle)
    # Set bin size which rectangles must be arranged in
    packer.add_bin(*canvasSize)
    # Arrange rectangles within the specified bin size
    packer.pack()

    packedRectangles = []
    # Build new list containing rectangle objects of type Rectangle
    for rectangle in packer.rect_list():
        rect = Rectangle(rectangle[4], rectangle[3], rectangle[1],
                         rectangle[2])
        packedRectangles.append(rect)
    # Return list of rectangles
    return packedRectangles


# Main function. This will execute when the program is run from the command
# line. Input expected is one command line argument, specifying the file
# containing the canvas size and rectangles to be placed within the canvas
def main():
    # Read in file
    with open(argv[1], 'r', encoding='utf-8') as input:
        fileContents = input.read().split('\n')
    # Gather height and width from first line
    height = int(fileContents[0].split(',')[0])
    width = int(fileContents[0].split(',')[1])
    canvasSize = (height, width)
    # Create canvas object
    canvas = CustomCanvas((height + 3), (width + 3))
    allRect = []
    # Iterate through each rectangle in file and create a rectangle object of
    # type Rectangle
    for index in range(1, len(fileContents)):
        rectangleSize = fileContents[index].split(',')
        rectangle = Rectangle(int(rectangleSize[0]), int(rectangleSize[1]))
        allRect.append(rectangle)
    # Pass list of rectangle objects created from the file input a long with the
    # specified canvas size
    packedRectangles = pack(allRect, canvasSize)
    # Add each rectangle to the canvas object
    for rectangle in packedRectangles:
        canvas.addRectangle(rectangle)
    # Pack canvas and display to user
    canvas.displayCanvas()


# Specifiy expected behavior if executed from command line
if __name__ == '__main__':
    main()
