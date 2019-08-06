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
			print('---------2---------------')
			answer = input('Add child to parent element? y/n\n')
			i = 0
		while answer == "y":

			print('Adding child #' + str(i) + ' at level: ' + str(self.level+1))
			child = ChildElement()
			child.setProperties(int(self.level+1))
			children.append(child)
			print('---------2---------------')
			i = i + 1
			answer = input('Add another child to parent element? y/n\n')
		self.children = children
