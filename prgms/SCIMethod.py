#In instance method use self as arg
#In class method use cls as arg (Use @classmethod decorator)
#In static method nothing (use @staticmethod decorator)

class student:
    school='telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchoolName(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class")

s1=student(12,34,12)
s2=student(23,56,12)

print(s1.avg())
print(student.getSchoolName())
student.info()
