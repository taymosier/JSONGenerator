from classes.ArrayElement import ArrayElement

class ArrayGenerator:
    def __init__(self):
        pass
    level = None
    length = None
    elements = []

    def setLevel(self, level):
        self.level = level

    def setLength(self):
        self.length = input('Please enter the length of the array')

    def setElements(self):
        newArray = []
        for i in range(self.length):
            element = ArrayElement(level+1, input('Please enter the type of element value'))
            element.setArrayItemValue()
        return newArray
