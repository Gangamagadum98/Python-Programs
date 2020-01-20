class Flat:
    BHk=3
    location="basavangudi"
    price=400000
    doorNo=1

    def shelter(self):
        print("providing shelter")

    def changeDoorNo(self,door):
        self.doorNo=door

ground=Flat()
ground.price="82lks"
print(ground.price)
ground.shelter()
ground.changeDoorNo(101)
print(ground.doorNo)

firstflr=Flat()
firstflr.price="40lks"
print(firstflr.price)
firstflr.shelter()
firstflr.changeDoorNo(102)
print(firstflr.doorNo)


secondflr=Flat()
secondflr.price="80lks"
print(secondflr.price)
secondflr.shelter()
secondflr.changeDoorNo(103)
print(secondflr.doorNo)

