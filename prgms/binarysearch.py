
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['pos']=mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u=mid



list = [2,34,56,78,234]
n = 56

if search(list, n):
    print("found",pos+1)
else:
    print("not found")