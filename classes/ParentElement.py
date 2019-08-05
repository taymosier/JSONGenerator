import numpy as np
from classes.ChildElement import ChildElement

class ParentElement:
  def __init__(self):
      pass
  type = None
  children = []
  level = 0

  def setType(self):
      self.type = input('Please enter the parent element type: array/object\n')

  def addChildren(self):
    if self.type == "array":
        pass
    elif self.type == "object":
        children = []
        answer = input('Add child to parent element? y/n\n')
        while answer == "y":
            print('adding child at level: ' + str(self.level+1))
            child = ChildElement()
            child.setLevel(self.level+1)
            child.setProperties()
            children.append(child)
            answer = input('end of ParentElement.addChildren\n Add another child? y/n\n')
        self.children = children
