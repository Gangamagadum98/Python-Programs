# 2 classes has same method and arguments and child class should inherit from parent .. child method can change the implementatn
# child method overrides the parent method

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")


a=B()
a.show()