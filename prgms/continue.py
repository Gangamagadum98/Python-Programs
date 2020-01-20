#printing except divisible by 3 or 5
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)
print("bye")

# printing except odd numbers
for j in range(1,101):
    if(j%2!=0):
        continue
    print(j)

# using pass
for k in range(1,101):
    if(k%2!=0):
        pass
    else:
        print(k)
