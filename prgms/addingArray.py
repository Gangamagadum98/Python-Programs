from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([9,4,3,2,2])
arr = arr1+5
print(arr)
print(sum(arr))     #sum of array
print(sqrt(arr))    # sqrt of array
print(log(arr))
print(sin(arr))
print(cos(arr))
print(min(arr1))
print(max(arr1))
arr3=arr1+arr2
print(arr3)
print(concatenate([arr1,arr2]))
print(sort(arr2))

#copying from one array to another array

arr1=array([2,5,7,8])
arr2=arr1
print(arr2)
print(id(arr1))     #to find address of array use id()
print(id(arr2))     # we copied array so both pointing to same address

#If want to point both address to be different
arr3=array([3,5,4,2,1,2])
arr4=arr3.view()        #use view() to pint with diff address even if array has same content

print(arr3)
print(arr4)
print(id(arr4))
print(id(arr3))

#shallow copy (we use view())
x=array([2,3,4,5])
y=x.view()
print(x)
print(y)
x[2]=10
print(x)
print(y)

#Deep copy (we use copy())
x=array([2,3,4,5])
y=x.copy()
print(x)
print(y)
x[2]=10
print(x)
print(y)

#assignmt addition of two array
from array import *
p=array('i',[1,2,3,4])
q=array('i',[2,3,4,5])
k=array('i',[])
for i in range(0,len(p)):
    print(i)
    k.append(p[i]+q[i])
print(k)

#Finding maximum value from array
z=array('i',[5,9,1,2,4])
k=sort(z)
print(k[len(z)-1])







