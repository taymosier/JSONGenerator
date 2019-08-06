

class ArrayElement:
	def __init__(self):
		pass

	level = None
	valueType = None
	value = None
	children = []

	def setProperties(self, level):
		self.setLevel(level)
		self.setValueType()
		self.setValue()

	def setLevel(self, level):
		self.level = level

	def setValue(self):
		if self.valueType == "string":
			self.value = input('please enter arrray item value')
		elif self.valueType == "object":
			answer = input('Add child to array element object? y/n')
			while answer == "y":
				self.children.append(self.generateChild())
				self.value = self.children
				answer = input('add another child to array element object?')
		elif self.valueType == "array":
			newArray = []
			answer = input('add item to array?\n')
			while answer == "y":
				element = ArrayElement()
				element.setProperties(self.level+1)
				newArray.append(element)
				answer = input('Add another item to array\n?')
			self.value = newArray

	def setValueType(self):
		self.valueType = input('Please enter the type of value\n')

	def generateChild(self):
		from classes.ChildElement import ChildElement
		child = ChildElement()
		child.setProperties(self.level+1)
		return child
