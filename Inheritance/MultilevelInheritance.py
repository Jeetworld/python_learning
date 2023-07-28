class A:
    def a(self):
        print("this is method a")

class B(A):
    def b(self):
        print("this is method from b")

class C(B):
    def c(self):
        print("this is method from c")


obj = C()
obj.c()
obj.a()
obj.b()
