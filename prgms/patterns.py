#Square
for i in range(4):
    for j in range(4):
        print("#", end=" ")
    print()

#Traiangle
for k in range(4):
    for l in range(k+1):
        print("#", end=" ")
    print()

# Reverse Triangle
for m in range(4):
    for n in range(4-m):
        print("#",end = "  ")
    print()

#number
for p in range(1,5):
    for q in range(p,5):
        print(q,end=" ")
    print()

#alphabate
str1='ABCD'
str2='PQR'
for i in range(4):
    print(str1[:i+1]+str2[i:])


