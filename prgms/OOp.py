# python supports Functional programing, procedure oriented programing and also object oriented programing. (ex-lambda)
# object - Instance of class (by using class design we can create no of obj)
# class - Its a design (blue print) (In class we can declare variables and methods)

class computer:

    def __init__(self,cpu,ram):
        print("init")            #__init_() its like constructor, it vl execute automaticaly without calling for eact object.
        self.cpu=cpu
        self.ram=ram


    def config(self):
        print("i5 16Gb 1Tb",self.cpu,self.ram)


com1=computer("i3",3)
com2 = computer("i5",4)
computer.config(com1)
computer.config(com2)
#or
com1.config()
com2.config()           #Internally config method takes com2 as argumt and pass it in config function