import  math
def jump_search(a, elem):

    n = len(a)
    prev = 0
    step = math.sqrt(n)

    # finding range

    while a[int(min(step, n-1))] < elem:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # finding index

    while a[int(prev)] < elem:
        prev += 1

        if prev == min(step, n):
            return -1
    if a[int(prev)] == elem:
        return prev

    return -1

index = jump_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],1)
if index == -1:
    print("not found")
else:
    print("found" , int(index))










