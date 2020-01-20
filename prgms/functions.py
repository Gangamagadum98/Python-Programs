# write any no of functions and call it
# function is a block have 1 task (always have 1 task for 1 functn and call)
def greet():
    print("hi")
    print("hello")

greet()

def add(x,y):
    c=x+ y
    print(c)
add(5,4)

# return value from function
def add(x,y):
    c=x+y
    return c
result = add(1,2)
print(result)

# return 2 value from function
def add_sub(x,y):
    z=x+y
    k=x-y
    return z, k
result1, result2 = add_sub(1,3)
print(result1, result2)

#update the function value
def update(x):
    x=8
    print(x)
update(10)

# Keyword arguments
def person(name,age):
    print(name)
    print(age)
person(age=20,name='Ganga')

#Default argument
def person(name,age=18):
    print(name)
    print(age)
person('Gnaga')

#Variable length arg

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
sum(5,6,34,78)

def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person('Ganga', age=20,city='karnataka',mob=8310383224)