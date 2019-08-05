class ArrayElement:
    def __init__(self):
        pass

    level = None
    type = None
    value = None
    valueType = None

    def setArrayItemValue(self):
        if self.type == "string":
          self.value = input('please enter arrray item value')
        elif self.type == "object":
          self.value = generateChild()
        elif self.type == "array":
          self.value = None

    def generateChild(self):
        return None

    def setArrayItemValueType(self, valueType):
        pass
