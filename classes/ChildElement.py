from generators.ArrayGenerator import ArrayGenerator
from classes.ArrayElement import ArrayElement

class ChildElement:
  def __init__(self):
    pass

  level = None
  value = None
  valueType = None
  key = None #str
  children = []

  def setLevel(self, level):
      self.level = level

  def setProperties(self):
      self.valueType = self.setValueType()
      self.key = self.setKey()
      print('setting value')
      self.value = self.setValue()

  def setKey(self):
       return input('Please enter the element key\n')

  def setValueType(self):
      return input('Please enter object, array, or string for ChildElement.valueType at level ' + str(self.level) + "\n")

  def setValue(self):
      if self.valueType == "string":
          return input('Please enter a string value\n')
      elif self.valueType == "object":
          answer = input('childElement.setValue Add child to object? y/n \n')
          i=0
          while answer == "y":
              print("Generating new child object " + str(i+1) + " on level: " + str(self.level+1))
              child = ChildElement() #instantiates new childElement()
              child.setLevel(self.level+1)
              child.setProperties()
              self.children.append(child)
              i = i+1
              answer = input('end of ChildElement.setvalue at level ' + str(self.level) + '\n add another child? y/n \n')
          return self.children
