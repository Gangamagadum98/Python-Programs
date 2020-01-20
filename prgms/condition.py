i =1

while i<=5:
    print("Hi", end="  ")
    j=1
    while(j<=5):
        print("Nikita", end=" ")
        j=j+1
    i=i+1
    print()

# for else

nums=[12,14,16,10,50]
for num in nums:
    if num%5 == 0:
        print(num)
        break
print("not found")