from numpy import *

arr1 = array([[1,2,3,4,5,6],[3,4,5,6,7,8]])
print(arr1.ndim)        # ndim gives no of dimension
print(arr1.dtype)       # dtype gives type of array
print(arr1.shape)       # gives no of rows and columns
print(arr1.size)        # gives size

#convert 2d array to 1d arrray
arr2=arr1.flatten()
print(arr2)

#convert 1d array to 3d array
arr3=arr2.reshape(3,4)
print(arr3)

arr3 = arr2.reshape(2,2,3)
print(arr3)

