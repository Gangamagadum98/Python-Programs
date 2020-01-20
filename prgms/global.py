a=10
def something():
    a=15
    print('local',a)
something()
print('Global', a)

# change global variable by using global keyword

a=10
def something():
    global a
    a=20
    print(a)
something()
print(a)

# keep local variable also as 'a' and change global variable also 'a'

a=10
print(id(a))
def something():
    a=9
    x=globals()['a']    #globals()- it vl gv all global values
    print(id(x))
    print('in fun',a)

    globals()['a']=15   #changing global value

something()
print('out fun',a)

#pass list to function

lst=[]
n = int(input("enter length of list"))
for i in range(n):
    x=int(input("Enter next value"))
    lst.append(x)
    print(lst)

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd= count(lst)
print("Even:{} and Odd:{}".format(even,odd))

