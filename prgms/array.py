from array import *

# int type array (start with -ve)
vals = array('i',[5,9,-3,1,0])
print(vals)
print(vals.buffer_info())           #buffer_info() gives size of array (address,size)

#unsigned type array start with 0
val = array('I',[6,9,0,4])
print(val)
print(val.buffer_info())

#reverse the array
val.append(5)
print(val)

#remove the array
val.remove(6)
print(val)

#reverse the array
val.reverse()
print(val)
print(val[1])

for i in range(4):
    print(vals[i])

for e in vals:
    print(e)

# char array
char = array('u',['a','e','i'])
print(char)

# creating new array from existing array

value = array('i',[3,9,2,1])
newArr = array(value.typecode,(a*a for a in value))
for e in newArr:
    print(e)

# user enters value to array

arr= array('i',[])
n= int(input("Enter the length of the array"))
for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)
# print(arr)

# search value in array
vall = int(input("Enter the value for search"))
k=0
for e in arr:
    if e==vall:
        print(k)
        break
    k+=1

#search by using function
print(arr.index(vall))



