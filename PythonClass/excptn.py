class Temp:
    name="Ganga"

temp=Temp()
#print(temp.name)

try:
    print("Entering try block")
    raise NameError("name error")
except:
    raise OverflowError("I am throwing overflow error")
finally:
    print("Hii")

    
