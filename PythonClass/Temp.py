class Temp:
    name="Ganga"

temp=Temp()
#print(temp.name)

try:
    print("Entering try block")
    print(temp.salary)
    raise NameError("")
except TypeError:
    print("I am in except block")

except :
    print("I am in except ")
finally:
    print("Hi we are learning Exception handling")
    try:
        print("Hi we are learning Exception handling")
    except:
        print("Hi we are learning Exception handling")  
print("Hi we are learning Exception handling")  


    
