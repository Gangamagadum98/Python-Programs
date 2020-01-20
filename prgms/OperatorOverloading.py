# WE have diff methods for diff operators
# __add__(), __sub__(), __mul__() call as 'magic methods'
# a=5
# b=6
# print(a+b)        Its possible with help of int/string bt no with class/obj
# print(int.__add__(a,b))


class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2=  m2

    def __add__(self,other):
        m1=self.m1 +other.m1
        m2=self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)


s1=Student(34,23)
s2=Student(13,14)

s3=s1+s2 #addition using '+' operator with class is not possible
# this code connverted into (Student.__add__(s1,s2)) here s1 is self and s2 is other in __add__ method
print(s3.m1)


# compare

if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')

a=12
print(a)        # indirectly its calling (a.__str__()) method

print(s1)
print(s2)


# --- Operator overloading --
# operator like +,-,*  operator vl remain same operands vl change and type of parameter vl change
# __add__() takes diff type of parameter/arguments
# Same method name bt no of arguments/ type of args are diff.