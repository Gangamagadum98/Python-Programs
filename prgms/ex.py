from array import *

def fact(x):
        fact = 1
        for i in range(1,x+1):
            fact= fact*i
        return fact


result = fact(4)
print(result)


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


result1  =fact(4)
print(result1)







def fib(n):
    a=0
    b=1
    if n==1:
        return a
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b       #1
        a=b         #1
        b=c         #1
        print(c)
fib(4)

arr= array('i',[1,2,3,4])
print(arr)
arr.append(8)
print(arr)
arr.reverse()
print(arr)
arr.insert(2,7)
print(arr)

arr1=array('i',[])
n=int(input("enter the length of array"))
for i in range(n):
    x=int(input("enter next element"))
    arr1.append(x)
    print(arr1)
z=int(input("enter search value"))
for e in arr1:
    if e==z:
        print(e)
        print('index',arr1.index(e))

x=array('i',[3,5,2])
y=array('i',[4,1,6])
z=array('i',[])
for i in range(len(x)):
    z.append(x[i]+y[i])
print(z)














