# If u define variable inside __init__ means its instance variable,
# If u change object of one variable it vl affect only that variable
#If you declare variable outside __init__ and inside class then it is static/Class variable.
# instance variable


class car:

    wheels = 4  #class variable

    def __init__(self):
        self.mil=10         #---|
        self.com="BMW"      #---|   both are instance variables
c1=car()
c2=car()

c1.mil=8

car.wheels = 5      #shared by all objects of the class

print(c1.com,c1.mil, c1.wheels)
print(c2.com,c2.mil, c2.wheels)