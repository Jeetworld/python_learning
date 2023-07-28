class ClassA:
    def showA(self):
        print("this is show A")

class ClassB(ClassA):   #simple inheritance
    def showB(self):
        print("this is show B")


obj = ClassB()
obj.showB()
obj.showA()
