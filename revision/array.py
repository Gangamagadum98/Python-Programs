from array import *
vals = array('i',[2,6,4,3])
print(vals.buffer_info())
vals.append(9)
print(vals)
vals.reverse()
print(vals)
for i in range(4):
    print(vals[i])
for e in vals:
    print(e)

value = array('i',[3,2,1,4,5,6,7])
newarr = array(value.typecode,(a*a for a in value))
print(newarr)

arr = array('i',[])
n = int(input("enter length of array"))
for i in range(n):
    a  = int(input("enter next no"))
    arr.append(a)
print(arr)
x = int(input("enter no to search"))
k=0
for i in arr:
    if(x==i):
        print(k)
        break
    k+=1


y = array('i',[])
z=int(input("enter length"))
for i in range(z):
    x=int(input("enter nxt no"))
    y.append(x)
print(y)
d=int(input("enter no to delete"))
for e in y:
    if e==d:
        continue
    else:
        print(e)
