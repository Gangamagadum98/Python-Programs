# Method Resolution Order (MRO)
# whenever it is multiple inheritance it goes from left to right that y it called A
class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1A working")

    def feature2(self):
        print("Feature 2 working")

class B:
    def __init__(self):
        super().__init__()
        print("In B Init")

    def feature1(self):
        print("Feature 3B is working")

    def feature2(self):
        print("Feature 4 is working")

class c(A,B):
    def __init__(self):
        super().__init__()
        print("In c Init")

class D(A):
    def feat(self):
        super().feature2()




a1=c()
a1.feature1()

d=D()
d.feat()