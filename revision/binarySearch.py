def binary_search(a, elem):
    mid = len(a) // 2
    if a[mid] == elem:
        return mid

    elif a[mid] > elem:
        print("Elements on LHS")
        for i in range(0, mid-1):
            if a[i] == elem:
                return i
    else:
        print("Element is on RHS")
        for i in range(mid+1, len(a)):
            if a[i] == elem:
                return  i
    return -1


index = binary_search([1, 2, 3, 4, 5], 5)
if index == -1:
    print("Element is not found in the array")
else:
    print("The index of elemene is" + str(index))
