# for displyaing 2 dimensional array its not possible with importing array, so install numpy using(pip install numpy) and import it
from numpy import *
arr = array([1,2,3,4,4])
print(arr)

#In linspace gap btw 2 elems is same
arr = linspace(0,15,16)         # 0-start, 15-end, 16-it vl give path from 0 to 15 that all in floats bcz values are divide by 16
print(arr)

#arange (2 vl give steps from 1 to 15 it vl display by skipping 2 steps
arr=arange(1,15,2)
print(arr)

#logspace (it vl start from 10^1 to 10^40 and divide by 5)
arr=logspace(1,40,5)
print('%.2f' %arr[0])

#Zeros

arr=zeros(5)
print(arr)

#ones
arr=ones(4)
print(arr)

arr=ones(4,int)
print(arr)