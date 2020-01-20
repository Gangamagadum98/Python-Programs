
# inserting element in position
def insertion_sort(a,n,pos):
    for j in a:
        print(j)
        # print(j)
        b=[]
        if pos<=len(a):
            for i in range(j):
                print(i)
                if pos==i:
                    b[i]=n
                else:
                    b=a
                    j+=1
    print(b)

a = [3,6,7,1,2]
insertion_sort(a,5,2)