#Single level inheritance
class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

a=A()
a.feature1()
a.feature2()

b=B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()