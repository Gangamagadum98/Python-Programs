from array import *
#assignmt Deleting no in array
arr1 = array('i',[])
a= int(input("enter the size of the array"))
for i in range(a):
    y=int(input('enter the next value'))
    arr1.append(y)


n= int(input("enter the no to delete"))

for e in arr1:
    if n==e:
        continue
    else:
        print(e)

# reverse of array
#Initialize array
arr = [1, 2, 3, 4, 5];
print("Original array: ");
for i in range(0, len(arr)):
    print(arr[i]),
print("Array in reverse order: ");
#Loop through the array in reverse order
for i in range(len(arr)-1, -1, -1):
    print(arr[i])







