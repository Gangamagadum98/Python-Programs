from abc import ABC
class Business(ABC):
    cost="201k"
    profit="101k"

    def _init_(self):
        print("inside business init")

    def sell(self):
        print("selling products")

class RealEstate(Business):
    commission="yes"

    def _init_(self):
        #Business._init_(self)
        super()._init_()
        print("inside real estate init")

    def sell(self):
        print("selling Estate")

    def recieve(self):
        print("recieving Estate")

estate=RealEstate()
print(estate.cost, estate.profit)
estate.sell()
estate.recieve()
