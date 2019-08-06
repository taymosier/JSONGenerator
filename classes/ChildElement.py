from generators.ArrayGenerator import ArrayGenerator


class ChildElement:
	def __init__(self):
		pass
	
	level = None
	value = None
	valueType = None
	key = None #str
	children = []

	def setLevel(self, level):
		self.level = int(level)

	def setProperties(self, level):
		self.setLevel(level+1)
		self.setValueType()
		self.setKey()
		self.setValue()

	def setKey(self):
		self.value = input('Please enter the element key\n')

	def setValueType(self):
		self.valueType = input('Please enter object, array, or string for ChildElement.valueType at level ' + str(self.level) + "\n")

	def setValue(self):
		if self.valueType == "string":
			self.value = input(self.key+'Please enter a string value\n')
		elif self.valueType == "object":
			answer = input(self.key+': Add child to object? y/n \n')
			while answer == "y":
				print("Generating new child object " + str(i+1) + " on level: " + str(self.level+1))
				child = ChildElement() #instantiates new childElement()
				child.setProperties(self.level+1)
				self.children.append(child)
				answer = input('end of ChildElement.setvalue at level ' + str(self.level) + '\n add another child? y/n \n')
			self.value = self.children
		elif self.valueType == "array":
			newArray = []
			answer = input(self.key+'Add element to array?')
			while answer == "y":
				from classes.ArrayElement import ArrayElement
				element = ArrayElement() #instantiates new ArrayElement()
				element.setProperties(self.level+1)
				self.children.append(element)
				answer = input('Add another element to array?\n')
			self.value = self.children
