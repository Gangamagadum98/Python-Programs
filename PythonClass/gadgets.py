class Gadgets:



    def __init__(self,name,price):
        self.name=name
        self.price=price

    @classmethod
    def factory(cls,name,price):
        return cls(name,price)

    @staticmethod
    def communicate(name):
        return "Communicating with" + name



Tablet = Gadgets.factory("Tablet",1000)
print(Tablet.price)

print(Gadgets.communicate("  Mobile"))

