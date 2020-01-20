name="Manasa"
print(name)

def learningPython(x):

    print("we are learning python")
    print(x)
    return 12
num=learningPython(10)
print(num)

def sub(x,y):
    print(x-y)
sub(1,2)

def sub(a,b):
    return a-b

num1=sub(3,2)
print(num1)

def mul(a,b):
    return a*b
num2=mul(3,2)
print(num2)

def div(a,b):
    return a/b
num2=div(30,2)
print(num2)

def random(*x): #variable length arguemrnt
    print("inside the function")
    sum=0
    for y in x:
        #print(y)
        sum=sum+y

    return sum

result=random(10,20,30,40,50)
print(result)

def doubleSum(*x): #variable length arguemrnt
    print("inside the function")
    sum=0
    for y in x:
        #z=y*2
        #print(z)
        sum=sum+2*y

    return sum

result=doubleSum(1,2,3,4,5)
print(result)

def random(*x): #variable length arguemrnt
    print("inside the function")
    sum=0
    for y in x:
        #print(y)
        if(y%2==0):
            sum=sum+y
    return sum
result=random(1,2,4,5,6)
print(result)

def mul(a=1,b=2):
    return a*b
value=mul() #value=mul(1,2)
print(value)

def divide(a=20,b=40):
    print(a,b)
    return a/b
divresult=divide(b=30)
print(divresult)

add1=lambda x,y : x+y
result=add1(2,5)
print(result)

cube=lambda x : x*x*x
print(cube(4))

square=lambda x : x*x
#result1=square(20,24,32,12,7)
print(square(4))






