import numpy as np
from classes.ChildElement import ChildElement

class ParentElement:
	def __init__(self):
		pass
	level = None
	valueType = None
	children = []
  
	def setLevel(self):
		self.level = 0

	def setType(self):
		self.valueType = input('Please enter the parent element type: array/object\n')

	def addChildren(self):
		if self.valueType == "array":
			pass
		elif self.valueType == "object":
			children = []
			answer = input('Add child to parent element? y/n\n')
		while answer == "y":
			print('adding child at level: ' + str(self.level+1))
			child = ChildElement()
			child.setProperties(int(self.level+1))
			children.append(child)
			answer = input('end of ParentElement.addChildren\n Add another child? y/n\n')
		self.children = children
