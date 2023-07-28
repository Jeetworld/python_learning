class ClassA:
    a=10
    b=20
    def __init__(self):
        print("***This is constructor***")
    def methodOne(self):
        print("this is method one")

    def methodTwo(self,a,b):
        print("Values are ",a,b)

    def methodThree(self):
        print("values are",self.a,"another values ",self.b)

obj = ClassA()
obj.methodOne()
obj.methodTwo(100,200)
obj.methodThree()