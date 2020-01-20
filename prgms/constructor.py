class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def __init__(self):
        super().__init__()
        print("In B Init")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a1=B()