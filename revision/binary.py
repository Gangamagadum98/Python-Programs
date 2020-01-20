

def sort(li):
    for i in range(len(li)-1, 0, -1):
        for j in range(0, i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

def binary(li, num):
    mid = len(li) // 2
    if li[mid] == num:
        return mid
    elif li[mid] > num:

        for i in range(0, mid-1):
            if li[i] == num:
                return i
    else:
        for i in range(mid+1, len(li)):
            if li[i] == num:
                return i

    return -1


li = [4, 9, 1, 3, 5, 2, 8, 6]
num = 8
SORTED_LIST = sort(li)
print(SORTED_LIST)
index = binary(SORTED_LIST, num)
if index == -1:
    print("value not found")
else:
    print("value found at", index )