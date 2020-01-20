class Car:
    color="red"
    brand="BMW"

class SUV(Car):
    hillControl="yes"


class HatchBack(Car):
    pass

class Sedan(Car):
    pass

suvobj=SUV
print(suvobj.brand)

hb=HatchBack
print(hb.color)
print(hb.brand)


