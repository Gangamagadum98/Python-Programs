n=2
while(1):
    i=1
    while(i<=10):
        print("%dX%d=%d"%(n,i,n*i))
        i=i+1
    choice=int(input("choose your options press 0 for no"))
    if choice==0:
        break
    n=n+1
    