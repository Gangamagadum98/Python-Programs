from abc import ABC
class Transport(ABC):
    noOfSeats=50

    # @abstractmethod
    def transportation(self):
        pass

class Bus(Transport):
    conductor="yes"

class Flight(Transport):
    typeOfClass="business"
    

class Train(Transport):
    noOfCoaches=20
    def transportation(self):
        print("abc")

train=Train()
print(train.noOfCoaches)
train.transportation()

