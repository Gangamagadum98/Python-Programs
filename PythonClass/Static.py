class Bag:
    color= "Black" #Static
    def __init__(self,price):
        self.price=price  #non-static

WildCraft = Bag(1500)
print(WildCraft.color)
Fastrack = Bag(1400)
print(Fastrack.color)
print(Fastrack.price)