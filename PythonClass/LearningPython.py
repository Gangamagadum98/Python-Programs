name="Ganga"
#print(name)


def learnPython(x):
   # print("We are learning python")     
   # print(x)
    return 12                                                           
num=learnPython(10)
#print(num)

def add(a,b):
    return a+b
num1 =add(5,1)
#print(num1)

def sub(a,b):m1 =mul(5,4)
#print(num1)

def random(*x):
    #print("Inside the func")
    sum=0
    for y in x:
        sum=sum+y
    return sum
        
result=random(10,20,30,40,50)
#print(result) 

def random(*x):
    #print("Inside the func")
    sum=0
    for y in x:
        if y%2==0:
            sum=sum+y
    return sum
        
result=random(1,2,4,5,6)
print(result)


def mul(a,b=2):
    return a*b
value=mul(4)
print(value)


def divide(a=80,b=2):
    return a/b
res=divide(b=40)
print(res)



