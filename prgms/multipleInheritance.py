class A:
    def feature1(self):
        print("feature1 is working")

class B:
    def feature1(self):
        print("feature2 is working")

class C(A,B):
    def feature3(self):
        print("feature 3 is working")

a=A()
a.feature1()

b=B()
b.feature1()

c=C()
# c.feature1()
# c.feature1()
c.feature3()