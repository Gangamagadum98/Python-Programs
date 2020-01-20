class Juice:
    fruit="Orange"

    def __init__(self,fruitName):
        self.fruit=fruitName
        self.quantity=2

    def prepareJuice(self):
     print("preparing",self.fruit,"juices")

Manasa=Juice("Grapes")
Manasa.prepareJuice()
print(Manasa.quantity)
8
Anusha=Juice("Orange")
Anusha.prepareJuice()



