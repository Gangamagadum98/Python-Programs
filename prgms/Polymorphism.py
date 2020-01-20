# Ploy-many maorphism - forms
# In Ploymorphism there are 4 types- 1.Duck typing,
# 2.Operator Overloading, 3.Method Overloading 4.Method Overriding

#1. Duck typing

class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("COnvention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=MyEditor()

lap1 = Laptop()
lap1.code(ide)