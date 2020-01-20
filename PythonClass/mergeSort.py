# It wil divide the list in to single element


def merge_sort(x):

    if(len(x)>1):
        print(x)
        mid=len(x)//2
        b=x[:mid]
        c=x[mid:]

        merge_sort(b)
        merge_sort(c)
        print(b)
        print(c)

        i = j = k = 0
        while i<len(b) and j<len(c):
            if b[i]>c[j]:
                x[k]=c[j]
                j+=1
            else:
                x[k]=b[i]
                i+=1

            k+=1
            # print(x)
        while i<len(b):
            x[k]=b[i]
            k+=1
            i+=1
        while j<len(c):
            x[k]=c[j]
            j+=1
            k+=1
    print(x)









x=[5,1,9,2]
merge_sort(x)