#Abstraction
from abc import (ABC,abstractmethod)
class Transport(ABC):
    noOfSeats=50

    @abstractmethod
    def transportation(self):
        pass
    
class Bus(Transport):
    conductor="yes"

    
class Flight(Transport):
    typeOfClass="buissness"
    

class Train(Transport):
     noOfCoaches=20
     def transportation(self):
         print("Passengers are travelling")


t=Train()
print(t.noOfCoaches)
t.transportation()

