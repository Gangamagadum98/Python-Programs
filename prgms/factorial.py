def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

x=3
result=fact(x)
print(result)

#Recurssion (a function Calling itself)
import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i=0
def welcom():
    global i
    i+=1
    print('Hello', i)
    welcom()
welcom()

#Factorial using recurssion

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)


result=fact(5)
print(result)