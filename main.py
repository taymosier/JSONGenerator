from classes.ParentElement import ParentElement

parent = ParentElement()

print('---------1---------------')
parent.setType()
parent.setLevel()
print('---------1---------------\n')
parent.addChildren()


for i in range(len(parent.children)):
    if type(parent.children[i].value) == list:
        for j in range(len(parent.children[i].value)):
            print(parent.children[i].value[j].value)
    print(str(parent.children[i].key) + " " + str(parent.children[i].value) + '\n')

    print()
