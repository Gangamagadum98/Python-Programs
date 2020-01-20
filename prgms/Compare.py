class computer:

    def __init__(self):
        self.name='navin'
        self.age=28

    def compare(self,x):
        if self.age==x.age:
            return True
        else:
            return False

c1=computer()
c2=computer()
c1.age=45
if c1.compare(c2):
    print("they are same")
else:
    print("They are diff")
print(c1.name)
print(c1.age)
