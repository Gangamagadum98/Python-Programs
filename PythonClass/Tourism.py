#from abc import ABC
class Tourism():
    noOfDays=5


    def package(self):
        print("3 days and 2 nights for Rs 5000")
    
                                                                                                                                           
class NorthIndia(Tourism):
    noOfDays = 7

    def package(self):
        print("3 days and 2 nights for Rs 5000")
    
class SouthIndia(Tourism):
    noOfDays = 7
    def package(self):
        print("3 days and 2 nights for Rs 10000")


north=NorthIndia()
north.package()

south=SouthIndia()
south.package()


    
    
    



