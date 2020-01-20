from numpy import *

m= matrix('1,2,3;4,5,6;7,8,9')          #put ; to display in next row
print(m)
print(m.diagonal())
print(m.min())
print(m.max())

#addition of matrix
m1=matrix('1,2,3;4,5,6;1,6,7')
m2=matrix('3,4,5;6,7,8;1,2,5')
m3=m1+m2
print(m3)
m4=m1*m2
print(m4)