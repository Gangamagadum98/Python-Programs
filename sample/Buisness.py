#Inheritance

class Buisness:
    cost="20lk"
    profit="10lk"

    def __init__(self,newCost):
        self.cost=newCost
        print("inside buisness init")
        print(self.cost)

    def sell(self):
        print("selling Products")


class RealEstate(Buisness):
    commission="yes"

    def __init__(self):
        Buisness.__init__()
        #super().__init__("1cr")
        print("inside real estate init")
    #def __init__(self,RLprofit,cost):
        #self.profit=RLprofit
        #self.cost=cost
    def sell(self):
        print("selling Estate")


class Restaurent(Buisness):
    partyHall="yes"

    def __init__(self):
        print("inside restaurent init")


#Rlobj=RealEstate("30lk","70lk")
Rlobj=RealEstate()
print(Rlobj.cost,Rlobj.profit)
Rlobj.sell()

Rsobj=Restaurent()
print(Rsobj.cost)
print(Rsobj.profit)
Rsobj.sell()