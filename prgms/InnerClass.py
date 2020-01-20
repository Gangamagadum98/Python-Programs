class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap = self.laptop() #creted obj of inner class inside outer class

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1=student('navin',2)
s2=student('gagana',1)

s1.show()

print(s1.lap.brand) #or
s1=s1.lap
s2=s2.lap
print(s1.brand)

lap1=student.laptop()       #creating inner class object outside outer class