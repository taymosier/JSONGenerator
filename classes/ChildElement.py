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
		self.setLevel(level)
		self.setValueType()
		self.setKey()
		self.setValue()

	def setKey(self):
		self.key = input('Please enter the element key\n')

	def setValueType(self):
		self.valueType = input('Please enter object, array, or string for ChildElement.valueType at level ' + str(self.level) + "\n")

	def printKeyValuePairs(self):
		print('\n'+self.key+':\n')
		for i in range(len(self.children)):
			if hasattr(self.value[i], "key"):
				print('Key: ' + str(self.value[i].key) + ' | Value: ' + str(self.value[i].value))

	def setValue(self):
		if self.valueType == "string":
			self.value = input('Please enter a string value for attribute: ' + self.key + '\n')
		elif self.valueType == "object":
			answer = input(self.key+': Add child to object? y/n \n')
			i = 0
			while answer == "y":
				self.printKeyValuePairs()
				print("\n-------------------------------------\nGenerating new child object " + str(i+1) + " on level: " + str(self.level+1) + '\n')
				child = ChildElement() #instantiates new childElement()
				child.setProperties(self.level+1)
				self.children.append(child)
				print('Child #' + str(i) + 'added to Attribute: ' + self.key)
				i = i + 1
				self.value = self.children
				answer = input('Add another child? y/n \n')
				print('-------------------------------------')
			print('There are ' + str(len(self.value)) + ' children in attribute: ' + self.key + '\n')

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
